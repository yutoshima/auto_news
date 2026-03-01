#!/usr/bin/env python3
"""
RSSHub パブリックインスタンスを使用したフィードテストスクリプト
"""

import feedparser
from datetime import datetime
import time

# テスト対象のRSSHubフィード
RSSHUB_FEEDS = {
    # AI企業（RSSが提供されていないソース）
    'Anthropic News (RSSHub)': 'https://rsshub.app/anthropic/news',

    # 他の候補（存在するか確認）
    'Google DeepMind (RSSHub)': 'https://rsshub.app/deepmind',
    'Tesla Blog (RSSHub)': 'https://rsshub.app/tesla/blog',

    # X（旧Twitter）アカウント例
    'Anthropic Twitter (RSSHub)': 'https://rsshub.app/twitter/user/AnthropicAI',
    'Tesla Twitter (RSSHub)': 'https://rsshub.app/twitter/user/Tesla',
}

def test_rsshub_feed(name: str, url: str, retry_count: int = 2):
    """RSSHubフィードをテスト（リトライ機能付き）"""
    print(f"\n{'='*70}")
    print(f"📡 テスト中: {name}")
    print(f"{'='*70}")
    print(f"URL: {url}")

    for attempt in range(1, retry_count + 1):
        if attempt > 1:
            print(f"\n🔄 リトライ {attempt}/{retry_count}...")
            time.sleep(2)  # レート制限対策

        try:
            print(f"\n⏳ フィードを取得中...")
            feed = feedparser.parse(url)

            # エラーチェック
            if feed.bozo:
                print(f"⚠️  警告: フィード解析に問題があります")
                if hasattr(feed, 'bozo_exception'):
                    error_msg = str(feed.bozo_exception)
                    print(f"   エラー詳細: {error_msg}")

                    # よくあるエラーパターンの説明
                    if '404' in error_msg or 'Not Found' in error_msg:
                        print(f"   💡 このRSSHubルートは存在しないか、無効化されています")
                        return False
                    elif '403' in error_msg or 'Forbidden' in error_msg:
                        print(f"   💡 アクセスが拒否されました（IP制限の可能性）")
                    elif 'timeout' in error_msg.lower():
                        print(f"   💡 タイムアウトしました（サーバー負荷が高い可能性）")

            # 記事数チェック
            entry_count = len(feed.entries)
            if entry_count == 0:
                print(f"\n⚠️  記事が取得できませんでした")

                # HTTPステータスコードを確認
                if hasattr(feed, 'status'):
                    print(f"   HTTPステータス: {feed.status}")
                    if feed.status == 404:
                        print(f"   💡 このRSSHubルートは存在しません")
                        return False
                    elif feed.status == 403:
                        print(f"   💡 アクセスが拒否されました")
                    elif feed.status >= 500:
                        print(f"   💡 RSSHubサーバーエラー（一時的な問題の可能性）")

                if attempt < retry_count:
                    continue  # リトライ
                return False

            # フィード情報の表示
            print(f"\n📰 フィード情報:")
            print(f"   タイトル: {feed.feed.get('title', 'N/A')}")
            description = feed.feed.get('description', feed.feed.get('subtitle', 'N/A'))
            print(f"   説明: {description[:100]}...")
            print(f"   記事数: {entry_count} 件")

            # 最新3件の記事を表示
            print(f"\n📝 最新記事（最大3件）:")
            for i, entry in enumerate(feed.entries[:3], 1):
                title = entry.get('title', 'タイトルなし')
                print(f"\n   [{i}] {title[:80]}")

                # 公開日時の取得
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    pub_date = datetime(*entry.published_parsed[:6])
                    print(f"       公開日: {pub_date.strftime('%Y-%m-%d %H:%M')}")
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    pub_date = datetime(*entry.updated_parsed[:6])
                    print(f"       更新日: {pub_date.strftime('%Y-%m-%d %H:%M')}")
                else:
                    print(f"       公開日: 不明")

                # URL
                link = entry.get('link', 'N/A')
                print(f"       URL: {link[:80]}...")

                # 概要
                summary = entry.get('summary', entry.get('description', '概要なし'))
                # HTMLタグを簡易的に除去
                import re
                summary_clean = re.sub(r'<[^>]+>', '', summary)
                print(f"       概要: {summary_clean[:120]}...")

            print(f"\n✅ {name}: 正常に取得できました")
            print(f"   💡 このRSSHubルートは使用可能です")
            return True

        except Exception as e:
            print(f"\n❌ エラーが発生しました")
            print(f"   エラー内容: {str(e)}")

            if attempt < retry_count:
                continue  # リトライ

            import traceback
            print(f"\n詳細なエラー情報:")
            traceback.print_exc()
            return False

    return False

def main():
    """すべてのRSSHubフィードをテスト"""
    print("="*70)
    print("🔍 RSSHub パブリックインスタンス テスト")
    print("="*70)
    print("\n📌 注意事項:")
    print("   - パブリックインスタンスは共有サーバーのため、")
    print("     アクセス制限やレート制限を受ける可能性があります")
    print("   - 404エラーの場合、そのRSSHubルートは存在しません")
    print("   - 本番運用にはセルフホストを推奨します")
    print()

    results = {}
    for i, (name, url) in enumerate(RSSHUB_FEEDS.items(), 1):
        print(f"\n進捗: {i}/{len(RSSHUB_FEEDS)}")
        results[name] = test_rsshub_feed(name, url)

        # レート制限対策（次のテストまで少し待機）
        if i < len(RSSHUB_FEEDS):
            print("\n⏳ 次のテストまで3秒待機中...")
            time.sleep(3)

    # 結果サマリー
    print(f"\n{'='*70}")
    print("📊 テスト結果サマリー")
    print(f"{'='*70}\n")

    success_count = sum(results.values())
    total_count = len(results)

    # カテゴリ別表示
    print("【AI企業（公式RSSなし）】")
    ai_feeds = [k for k in results.keys() if 'Anthropic News' in k or 'DeepMind' in k]
    for name in ai_feeds:
        if name in results:
            status = "✅ 使用可能" if results[name] else "❌ 使用不可"
            print(f"  {status} {name}")

    print("\n【企業ブログ（公式RSSなし）】")
    blog_feeds = [k for k in results.keys() if 'Blog' in k and 'Twitter' not in k]
    for name in blog_feeds:
        if name in results:
            status = "✅ 使用可能" if results[name] else "❌ 使用不可"
            print(f"  {status} {name}")

    print("\n【X（旧Twitter）アカウント】")
    twitter_feeds = [k for k in results.keys() if 'Twitter' in k]
    for name in twitter_feeds:
        if name in results:
            status = "✅ 使用可能" if results[name] else "❌ 使用不可"
            print(f"  {status} {name}")

    print(f"\n合計成功: {success_count}/{total_count} ({success_count/total_count*100:.0f}%)")

    if success_count > 0:
        print("\n✅ 使用可能なRSSHubルートが見つかりました！")
        print("   これらは news_collector.py に追加できます。")
        print("\n⚠️  ただし、パブリックインスタンスは以下のリスクがあります:")
        print("   - アクセス制限やIP制限を受けやすい")
        print("   - 取得エラーが頻発する可能性")
        print("   - 本番運用には不安定")
        print("\n💡 推奨: 安定した運用には Docker でのセルフホストを検討してください")
    else:
        print("\n⚠️  すべてのRSSHubルートが使用できませんでした。")
        print("\n考えられる原因:")
        print("   1. RSSHubルートが存在しない、または無効化されている")
        print("   2. パブリックインスタンスがIP制限を受けている")
        print("   3. 一時的なサーバー負荷")
        print("\n💡 解決策:")
        print("   1. RSSHub公式ドキュメントで正しいルートを確認")
        print("   2. 時間をおいて再テスト")
        print("   3. セルフホストの検討")

if __name__ == "__main__":
    main()
