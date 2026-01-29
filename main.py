#!/usr/bin/env python3
"""
車とITニュース自動配信システム - メイン実行スクリプト
"""

import argparse
from datetime import datetime
from news_collector import NewsCollector
from news_analyzer import NewsAnalyzer
from discord_notifier import DiscordNotifier


def main():
    """メイン処理"""

    parser = argparse.ArgumentParser(description='車とITニュース自動配信システム')
    parser.add_argument('--mode', choices=['all', 'new-cars', 'test'], default='all',
                        help='実行モード: all=全ニュース配信, new-cars=新型車のみ, test=接続テスト')
    parser.add_argument('--hours', type=int, default=24,
                        help='何時間前までのニュースを取得するか（デフォルト: 24時間）')

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

        # 接続テストモード
        if args.mode == 'test':
            print("🔧 接続テスト中...\n")
            if notifier.test_connection():
                print("✅ Discord接続: 成功")
            else:
                print("❌ Discord接続: 失敗")
            return

        # ニュース収集
        print("📡 ニュース収集を開始...\n")
        articles = collector.fetch_recent_news(hours_back=args.hours)

        if not articles:
            print("⚠️  新しいニュースが見つかりませんでした")
            notifier.send_daily_summary("本日は新しいニュースがありませんでした。")
            return

        print(f"✅ {len(articles)} 件の記事を取得しました\n")

        # 新型車専用モード
        if args.mode == 'new-cars':
            print("🔍 新型車情報の検索を開始...\n")

            # メーカー公式情報も追加取得
            manufacturer_articles = collector.get_manufacturer_news_only(hours_back=48)
            all_articles = articles + manufacturer_articles

            # 新型車判定
            new_cars = analyzer.analyze_all_for_new_cars(all_articles)

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

            # 日次サマリーの生成
            summary = analyzer.summarize_daily_news(articles, max_articles=10)

            print("要約結果:")
            print("-" * 60)
            print(summary)
            print("-" * 60)
            print()

            # Discord に送信
            print("📤 Discordに送信中...\n")
            success = notifier.send_daily_summary(summary)

            if success:
                print("✅ ニュース配信完了\n")
            else:
                print("❌ ニュース配信失敗\n")

            # 新型車情報も同時チェック
            print("🔍 新型車情報も同時チェック中...\n")
            new_cars = analyzer.analyze_all_for_new_cars(articles)

            if new_cars:
                print(f"🚨 {len(new_cars)} 件の新型車を追加で発見しました！\n")
                notifier.send_new_car_summary(new_cars)

        print("=" * 60)
        print("🎉 処理が完了しました")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ エラーが発生しました: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
