#!/usr/bin/env python3
"""
戦略的情報源（クラウド・半導体・AI）のRSSテストスクリプト
"""

import feedparser
from datetime import datetime

# テスト対象のRSSフィード
STRATEGIC_FEEDS = {
    # クラウド・インフラ公式ブログ
    'AWS What\'s New': 'https://aws.amazon.com/about-aws/whats-new/recent/feed/',
    'Microsoft DevBlogs': 'https://devblogs.microsoft.com/feed/',
    'GitHub Blog': 'https://github.blog/feed/',

    # 車載半導体・AIプラットフォーム
    'NVIDIA Newsroom': 'https://nvidianews.nvidia.com/releases.xml',

    # AI業界主要企業
    'OpenAI Blog': 'https://openai.com/blog/rss.xml',
}

def test_feed(name: str, url: str):
    """単一のRSSフィードをテスト"""
    print(f"\n{'='*70}")
    print(f"📡 テスト中: {name}")
    print(f"{'='*70}")

    try:
        feed = feedparser.parse(url)

        if feed.bozo:
            print(f"⚠️  警告: フィード解析に問題があります")
            if hasattr(feed, 'bozo_exception'):
                print(f"   エラー詳細: {feed.bozo_exception}")

        # フィード情報
        print(f"\n📰 フィード情報:")
        print(f"   タイトル: {feed.feed.get('title', 'N/A')}")
        print(f"   説明: {feed.feed.get('description', feed.feed.get('subtitle', 'N/A'))[:100]}...")
        print(f"   記事数: {len(feed.entries)} 件")

        if len(feed.entries) == 0:
            print(f"\n❌ 記事が取得できませんでした")
            return False

        # 最新3件の記事を表示
        print(f"\n📝 最新記事（最大3件）:")
        for i, entry in enumerate(feed.entries[:3], 1):
            title = entry.get('title', 'タイトルなし')[:80]
            print(f"\n   [{i}] {title}")

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

        print(f"\n✅ {name}: 正常に解析できました")
        return True

    except Exception as e:
        print(f"\n❌ {name}: エラーが発生しました")
        print(f"   エラー内容: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """すべてのフィードをテスト"""
    print("🔍 戦略的情報源（クラウド・半導体・AI）のRSSテストを開始します\n")

    results = {}
    for name, url in STRATEGIC_FEEDS.items():
        results[name] = test_feed(name, url)

    # 結果サマリー
    print(f"\n{'='*70}")
    print("📊 テスト結果サマリー")
    print(f"{'='*70}\n")

    success_count = sum(results.values())
    total_count = len(results)

    # カテゴリ別表示
    print("【クラウド・インフラ】")
    cloud_feeds = ['AWS What\'s New', 'Microsoft DevBlogs', 'GitHub Blog']
    for name in cloud_feeds:
        if name in results:
            status = "✅ OK" if results[name] else "❌ NG"
            print(f"  {status} {name}")

    print("\n【半導体・AIプラットフォーム】")
    if 'NVIDIA Newsroom' in results:
        status = "✅ OK" if results['NVIDIA Newsroom'] else "❌ NG"
        print(f"  {status} NVIDIA Newsroom")

    print("\n【AI企業】")
    if 'OpenAI Blog' in results:
        status = "✅ OK" if results['OpenAI Blog'] else "❌ NG"
        print(f"  {status} OpenAI Blog")

    print(f"\n合計成功: {success_count}/{total_count} ({success_count/total_count*100:.0f}%)")

    if success_count == total_count:
        print("\n🎉 すべてのフィードが正常に解析できました！")
        print("   news_collector.py に安全に追加できます。")
    else:
        print("\n⚠️  一部のフィードで問題が発生しました。")
        print("   問題のあるフィードのURLを確認してください。")

if __name__ == "__main__":
    main()
