#!/usr/bin/env python3
"""
車とITニュース自動配信システム - メイン実行スクリプト
"""

import argparse
from datetime import datetime
from news_collector import NewsCollector
from news_analyzer import NewsAnalyzer
from discord_notifier import DiscordNotifier
from article_storage import ArticleStorage
from github_trending import GitHubTrendingCollector, TrendingHistory, explain_repository


def main():
    """メイン処理"""

    parser = argparse.ArgumentParser(description='車とITニュース自動配信システム')
    parser.add_argument('--mode', choices=['all', 'new-cars', 'github-trending', 'test'], default='all',
                        help='実行モード: all=全ニュース配信, new-cars=新型車のみ, github-trending=GitHub Trending配信, test=接続テスト')
    parser.add_argument('--hours', type=int, default=24,
                        help='何時間前までのニュースを取得するか（デフォルト: 24時間）')
    parser.add_argument('--importance', type=int, default=3,
                        help='重要度の閾値（1-5、デフォルト: 3）この値以上の記事を配信')
    parser.add_argument('--alert-importance', type=int, default=4,
                        help='@everyoneで通知する重要度の閾値（1-5、デフォルト: 4）')
    parser.add_argument('--max-articles', type=int, default=10,
                        help='カテゴリごとに配信する最大記事数（デフォルト: 10）')
    parser.add_argument('--max-alerts', type=int, default=5,
                        help='カテゴリごとに@everyoneで通知する最大記事数（デフォルト: 5）')
    parser.add_argument('--trending-top', type=int, default=5,
                        help='GitHub Trendingで配信する上位リポジトリ数（デフォルト: 5）')
    parser.add_argument('--trending-min-stars', type=int, default=500,
                        help='初登場ランキングに載せる「今日増えたスター数」の下限（この値以下は除外、デフォルト: 500）')

    args = parser.parse_args()

    print("=" * 60)
    print("🚗💻 車とITニュース自動配信システム")
    print("=" * 60)
    print(f"実行時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"モード: {args.mode}")
    print("=" * 60)
    print()

    try:
        # 各モジュールの初期化
        collector = NewsCollector()
        analyzer = NewsAnalyzer()
        notifier = DiscordNotifier()
        storage = ArticleStorage()

        # 接続テストモード
        if args.mode == 'test':
            print("🔧 接続テスト中...\n")
            if notifier.test_connection():
                print("✅ Discord接続: 成功")
            else:
                print("❌ Discord接続: 失敗")
            return

        # GitHub Trending配信モード
        if args.mode == 'github-trending':
            send_github_trending(analyzer, notifier, args.trending_top, args.trending_min_stars)
            return

        # ニュース収集
        print("📡 ニュース収集を開始...\n")
        articles = collector.fetch_recent_news(hours_back=args.hours)

        if not articles:
            print("⚠️  新しいニュースが見つかりませんでした")
            notifier.send_daily_summary("本日は新しいニュースがありませんでした。", category='car')
            return

        print(f"✅ {len(articles)} 件の記事を取得しました\n")

        # 英語の記事を日本語に翻訳
        print("🌐 英語記事を日本語に翻訳中...\n")
        for i, article in enumerate(articles, 1):
            # タイトルの翻訳
            translated_title = analyzer.translate_to_japanese(article['title'])
            if translated_title != article['title']:
                print(f"  [{i}/{len(articles)}] 翻訳: {article['title'][:50]}... → {translated_title[:50]}...")
                article['title'] = translated_title

            # 概要の翻訳
            summary = article.get('summary', '')
            if isinstance(summary, list):
                summary = ' '.join(summary)
            if summary:
                translated_summary = analyzer.translate_to_japanese(str(summary))
                if translated_summary != summary:
                    article['summary'] = translated_summary

        print(f"✅ 翻訳完了\n")

        # 記事をMarkdownとして保存
        print("💾 記事をMarkdownとして保存中...\n")
        storage.save_articles(articles)
        print()

        # 新型車専用モード
        if args.mode == 'new-cars':
            print("🔍 新型車情報の検索を開始...\n")

            # メーカー公式RSSのみから取得済み（fetch_recent_news()で取得）
            # 新型車判定
            new_cars = analyzer.analyze_all_for_new_cars(articles)

            if new_cars:
                print(f"\n🚨 {len(new_cars)} 件の新型車を発見しました！\n")

                # Discord に送信
                for car in new_cars:
                    print(f"  📤 送信中: {car['manufacturer']} {car['model_name']}")
                    notifier.send_new_car_alert(car)

                print("\n✅ 新型車情報の配信完了\n")
            else:
                print("⚠️  新型車情報は見つかりませんでした\n")
                notifier.send_daily_summary("本日は新型車の発表はありませんでした。")

        # 全ニュース配信モード
        else:
            print("📝 ニュースの要約を開始...\n")

            # カテゴリ別に記事を分類
            it_articles = [a for a in articles if a.get('category') == 'it']
            car_articles = [a for a in articles if a.get('category') == 'car']

            # 重要度を評価（記事の中身で it / car を判定し直す）
            print(f"💻 IT記事 {len(it_articles)} 件を評価中...\n")
            analyzer.score_articles(it_articles)
            print(f"\n🚗 車記事 {len(car_articles)} 件を評価中...\n")
            analyzer.score_articles(car_articles)

            # 評価で判定したカテゴリで振り分け直す
            moved_to_car = sum(1 for a in it_articles if a.get('category') == 'car')
            moved_to_it = sum(1 for a in car_articles if a.get('category') == 'it')
            it_articles = [a for a in articles if a.get('category') == 'it']
            car_articles = [a for a in articles if a.get('category') == 'car']
            print(f"\n↪️  IT→車: {moved_to_car} 件 / 車→IT: {moved_to_it} 件 を振り分け直しました\n")

            # IT記事の要約と送信
            if it_articles:
                print(f"💻 IT記事 {len(it_articles)} 件を処理中...\n")
                it_summary = analyzer.summarize_daily_news(it_articles, importance_threshold=args.importance, max_top=args.max_alerts)

                # 重要記事が見つかった場合のみ送信
                if "重要度" not in it_summary or "ありませんでした" not in it_summary:
                    print("IT要約結果:")
                    print("-" * 60)
                    print(it_summary)
                    print("-" * 60)
                    print()

                    print("📤 ITチャンネルに送信中...\n")
                    it_success = notifier.send_daily_summary(it_summary, it_articles, category='it', importance_threshold=args.importance, max_articles=args.max_articles)

                    if it_success:
                        print("✅ IT記事配信完了\n")
                    else:
                        print("⚠️ IT記事の一部が配信できませんでした\n")

                    # 一部の記事が送れなくても重要ニュースの通知は送る
                    if notifier.send_important_alert(it_articles, category='it', alert_threshold=args.alert_importance, max_articles=args.max_alerts):
                        print("🚨 IT重要ニュース通知完了\n")
                else:
                    print(f"⚠️  重要度 ★{args.importance}/5 以上のIT記事はありませんでした\n")

            # 車記事の要約と送信
            if car_articles:
                print(f"🚗 車記事 {len(car_articles)} 件を処理中...\n")
                car_summary = analyzer.summarize_daily_news(car_articles, importance_threshold=args.importance, max_top=args.max_alerts)

                # 重要記事が見つかった場合のみ送信
                if "重要度" not in car_summary or "ありませんでした" not in car_summary:
                    print("車要約結果:")
                    print("-" * 60)
                    print(car_summary)
                    print("-" * 60)
                    print()

                    print("📤 車チャンネルに送信中...\n")
                    car_success = notifier.send_daily_summary(car_summary, car_articles, category='car', importance_threshold=args.importance, max_articles=args.max_articles)

                    if car_success:
                        print("✅ 車記事配信完了\n")
                    else:
                        print("⚠️ 車記事の一部が配信できませんでした\n")

                    # 一部の記事が送れなくても重要ニュースの通知は送る
                    if notifier.send_important_alert(car_articles, category='car', alert_threshold=args.alert_importance, max_articles=args.max_alerts):
                        print("🚨 車重要ニュース通知完了\n")
                else:
                    print(f"⚠️  重要度 ★{args.importance}/5 以上の車記事はありませんでした\n")

            # 新型車情報のチェックは new-cars モード専用
            # （時間がかかるため、全ニュースモードではスキップ）
            print("💡 新型車の詳細チェックは 'new-cars' モードで実行されます\n")

        print("=" * 60)
        print("🎉 処理が完了しました")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ エラーが発生しました: {str(e)}")
        import traceback
        traceback.print_exc()


def send_github_trending(analyzer, notifier, top: int, min_stars: int):
    """今日スターが増えたリポジトリの上位と、初めてTrendingに載ったリポジトリの上位を配信"""
    print("⭐ GitHub Trendingを取得中...\n")
    collector = GitHubTrendingCollector()
    repos = collector.fetch_repositories(since='daily')
    if not repos:
        print("⚠️  Trendingのリポジトリを取得できませんでした")
        return
    print(f"✅ {len(repos)} 件のリポジトリを取得しました\n")

    history = TrendingHistory()
    known = history.known_names()

    top_repos = repos[:top]
    # 履歴にないもののうち、今日のスター増加が min_stars を超えるものだけ
    new_repos = [r for r in repos if r['name'] not in known and r['stars_gained'] > min_stars][:top]

    print("📝 リポジトリの説明を作成中...\n")
    for repo in {r['name']: r for r in top_repos + new_repos}.values():
        repo['description'] = explain_repository(analyzer, repo, collector.fetch_readme(repo['name']))
        print(f"  {repo['name']}: {repo['description'][:60]}...")
    print()

    today = datetime.now().strftime('%Y年%m月%d日')
    print("📤 GitHub Trendingチャンネルに送信中...\n")
    notifier.send_github_trending(top_repos, f"⭐ GitHub スター急上昇 TOP{top} ({today})")
    notifier.send_github_trending(
        new_repos,
        f"🆕 Trending初登場 TOP{top}（+{min_stars}超） ({today})",
        empty_message=f"🆕 今日はTrending初登場で +{min_stars} を超えたリポジトリはありませんでした。",
    )

    # 配信後に履歴を更新（今回Trendingに載ったものはすべて既出扱いにする）
    history.record(repos)
    print("✅ GitHub Trending配信完了\n")


if __name__ == "__main__":
    main()
