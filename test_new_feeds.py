#!/usr/bin/env python3
"""
新しく追加したRSSフィードのテストスクリプト
"""

import feedparser
from datetime import datetime

# テスト対象のRSSフィード
TEST_FEEDS = {
    # IT関連
    'The Verge': 'https://www.theverge.com/rss/index.xml',
    'Hacker News': 'https://news.ycombinator.com/rss',

    # EV・自動車テックメディア
    'Electrek': 'https://electrek.co/feed/',
    'InsideEVs': 'https://insideevs.com/rss/articles/all/',

    # 自動車メーカー
    'Mercedes-Benz': 'https://group-media.mercedes-benz.com/marsMediaSite/en/instance/ko/RSS-Feeds.xhtml?oid=9266299',
    'Volvo': 'https://www.media.volvocars.com/global/en-gb/rss',
}

def test_feed(name: str, url: str):
    """単一のRSSフィードをテスト"""
    print(f"\n{'='*60}")
    print(f"📡 テスト中: {name}")
    print(f"{'='*60}")

    try:
        feed = feedparser.parse(url)

        if feed.bozo:
            print(f"⚠️  警告: フィード解析に問題があります")
            if hasattr(feed, 'bozo_exception'):
                print(f"   エラー詳細: {feed.bozo_exception}")

        # フィード情報
        print(f"\n📰 フィード情報:")
        print(f"   タイトル: {feed.feed.get('title', 'N/A')}")
        print(f"   説明: {feed.feed.get('description', 'N/A')[:100]}...")
        print(f"   記事数: {len(feed.entries)} 件")

        # 最新3件の記事を表示
        print(f"\n📝 最新記事（3件）:")
        for i, entry in enumerate(feed.entries[:3], 1):
            print(f"\n   [{i}] {entry.get('title', 'タイトルなし')[:80]}")

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
            print(f"       URL: {entry.get('link', 'N/A')[:80]}...")

            # 概要
            summary = entry.get('summary', entry.get('description', '概要なし'))
            print(f"       概要: {summary[:100]}...")

        print(f"\n✅ {name}: 正常に解析できました")
        return True

    except Exception as e:
        print(f"\n❌ {name}: エラーが発生しました")
        print(f"   エラー内容: {str(e)}")
        return False

def main():
    """すべてのフィードをテスト"""
    print("🔍 新規RSSフィードのテストを開始します\n")

    results = {}
    for name, url in TEST_FEEDS.items():
        results[name] = test_feed(name, url)

    # 結果サマリー
    print(f"\n{'='*60}")
    print("📊 テスト結果サマリー")
    print(f"{'='*60}\n")

    success_count = sum(results.values())
    total_count = len(results)

    for name, success in results.items():
        status = "✅ OK" if success else "❌ NG"
        print(f"{status} {name}")

    print(f"\n成功: {success_count}/{total_count} ({success_count/total_count*100:.0f}%)")

    if success_count == total_count:
        print("\n🎉 すべてのフィードが正常に解析できました！")
        print("   news_collector.py に安全に追加できます。")
    else:
        print("\n⚠️  一部のフィードで問題が発生しました。")
        print("   問題のあるフィードのURLを確認してください。")

if __name__ == "__main__":
    main()
