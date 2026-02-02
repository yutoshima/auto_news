#!/usr/bin/env python3
"""
RSS URL Discovery Tool

各メーカーのニュースルームから自動的にRSS URLを探索します。
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
import time


class RSSDiscovery:
    """RSS URLを自動発見するクラス"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })

        # 調査対象のメーカー（RSS取得失敗の11社）
        self.manufacturers = {
            'Toyota': 'https://global.toyota/en/newsroom/',
            'Lexus': 'https://pressroom.lexus.com/',
            'Honda': 'https://global.honda/en/newsroom/',
            'Mazda': 'https://www.mazda.com/en/',
            'Porsche': 'https://newsroom.porsche.com/en/',
            'General Motors': 'https://news.gm.com/',
            'Ford': 'https://media.ford.com/',
            'Tesla': 'https://ir.tesla.com/',
            'Hyundai': 'https://www.hyundainews.com/',
            'Lamborghini': 'https://media.lamborghini.com/',
            'Rolls-Royce': 'https://www.press.rolls-roycemotorcars.com/',
        }

    def discover_rss_url(self, name: str, base_url: str) -> dict:
        """
        特定のメーカーのRSS URLを発見

        Returns:
            {
                'found': bool,
                'rss_urls': list,
                'methods': list,  # どの方法で発見したか
                'page_url': str
            }
        """
        result = {
            'name': name,
            'base_url': base_url,
            'found': False,
            'rss_urls': [],
            'methods': [],
            'error': None
        }

        print(f"\n{'='*60}")
        print(f"🔍 {name} のRSS URLを探索中...")
        print(f"   URL: {base_url}")
        print(f"{'='*60}")

        try:
            # Method 1: HTML <link> タグから検索
            print(f"\n📄 Method 1: HTML <link> タグを確認中...")
            link_rss = self._find_rss_in_link_tags(base_url)
            if link_rss:
                result['rss_urls'].extend(link_rss)
                result['methods'].append('link_tag')
                result['found'] = True
                for url in link_rss:
                    print(f"   ✅ 発見: {url}")

            # Method 2: よくあるRSS URLパターンを試す
            print(f"\n📋 Method 2: 一般的なRSSパターンを試行中...")
            common_rss = self._try_common_rss_patterns(base_url)
            if common_rss:
                for url in common_rss:
                    if url not in result['rss_urls']:
                        result['rss_urls'].append(url)
                        result['methods'].append('common_pattern')
                        result['found'] = True
                        print(f"   ✅ 発見: {url}")

            # Method 3: ページ内のRSSリンクを検索
            print(f"\n🔗 Method 3: ページ内のRSSリンクを検索中...")
            page_rss = self._find_rss_links_in_page(base_url)
            if page_rss:
                for url in page_rss:
                    if url not in result['rss_urls']:
                        result['rss_urls'].append(url)
                        result['methods'].append('page_link')
                        result['found'] = True
                        print(f"   ✅ 発見: {url}")

            # 結果サマリー
            print(f"\n{'-'*60}")
            if result['found']:
                print(f"✅ {name}: {len(result['rss_urls'])} 個のRSS URLを発見しました")
                for i, url in enumerate(result['rss_urls'], 1):
                    print(f"   {i}. {url}")
            else:
                print(f"❌ {name}: RSS URLが見つかりませんでした")

        except Exception as e:
            result['error'] = str(e)
            print(f"⚠️  エラー: {str(e)}")

        time.sleep(2)  # レート制限
        return result

    def _find_rss_in_link_tags(self, url: str) -> list:
        """HTML <link> タグからRSS URLを検索"""
        rss_urls = []

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # <link rel="alternate" type="application/rss+xml"> を探す
            rss_links = soup.find_all('link', {
                'rel': 'alternate',
                'type': lambda x: x and 'rss' in x.lower() or x and 'atom' in x.lower()
            })

            for link in rss_links:
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)
                    rss_urls.append(full_url)

        except Exception as e:
            pass

        return rss_urls

    def _try_common_rss_patterns(self, base_url: str) -> list:
        """よくあるRSS URLパターンを試す"""
        rss_urls = []

        parsed = urlparse(base_url)
        base = f"{parsed.scheme}://{parsed.netloc}"

        # 一般的なRSSパターン
        patterns = [
            '/rss',
            '/feed',
            '/rss.xml',
            '/feed.xml',
            '/news/rss',
            '/news/feed',
            '/press-releases/rss',
            '/press-releases/feed',
            '/en/rss',
            '/en/feed',
            '/global/rss',
            '/global/feed',
            '/newsroom/rss',
            '/newsroom/feed',
        ]

        for pattern in patterns:
            test_url = base + pattern

            try:
                response = self.session.head(test_url, timeout=5, allow_redirects=True)

                # 200 OKまたはRSS/XMLのContent-Type
                if response.status_code == 200:
                    content_type = response.headers.get('Content-Type', '').lower()
                    if 'xml' in content_type or 'rss' in content_type or 'atom' in content_type:
                        rss_urls.append(test_url)
                        print(f"      試行: {pattern} → ✅")
                        continue

                # HEADで失敗した場合はGETも試す
                response = self.session.get(test_url, timeout=5)
                if response.status_code == 200:
                    # XMLっぽい内容か確認
                    if b'<?xml' in response.content[:100] or b'<rss' in response.content[:500]:
                        rss_urls.append(test_url)
                        print(f"      試行: {pattern} → ✅")

            except:
                pass

        return rss_urls

    def _find_rss_links_in_page(self, url: str) -> list:
        """ページ内のRSSリンクを検索"""
        rss_urls = []

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # "RSS" または "Feed" を含むリンクを探す
            all_links = soup.find_all('a', href=True)

            for link in all_links:
                href = link.get('href', '')
                text = link.get_text().lower()

                # RSSっぽいリンクを探す
                if ('rss' in href.lower() or 'feed' in href.lower() or
                    'rss' in text or 'feed' in text):

                    full_url = urljoin(url, href)

                    # .xml, .rss で終わる、またはrss/feedを含むURL
                    if (full_url.endswith(('.xml', '.rss')) or
                        '/rss' in full_url or '/feed' in full_url):

                        if full_url not in rss_urls:
                            rss_urls.append(full_url)

        except Exception as e:
            pass

        return rss_urls

    def discover_all(self) -> dict:
        """全メーカーのRSS URLを探索"""
        print("🚀 RSS URL自動探索を開始します")
        print(f"対象メーカー: {len(self.manufacturers)} 社\n")

        results = {}

        for name, url in self.manufacturers.items():
            result = self.discover_rss_url(name, url)
            results[name] = result

        return results

    def print_summary(self, results: dict):
        """探索結果のサマリーを表示"""
        print("\n" + "="*60)
        print("📊 RSS URL探索結果サマリー")
        print("="*60)

        found_count = sum(1 for r in results.values() if r['found'])
        total_count = len(results)

        print(f"\n✅ RSS URL発見: {found_count}/{total_count} 社")

        # 発見したメーカー
        if found_count > 0:
            print(f"\n【発見済み】")
            for name, result in results.items():
                if result['found']:
                    print(f"\n🎉 {name}")
                    for i, url in enumerate(result['rss_urls'], 1):
                        print(f"   {i}. {url}")
                    print(f"   発見方法: {', '.join(set(result['methods']))}")

        # 未発見のメーカー
        not_found = [name for name, r in results.items() if not r['found']]
        if not_found:
            print(f"\n【未発見】")
            for name in not_found:
                print(f"   ❌ {name}")
                if results[name]['error']:
                    print(f"      エラー: {results[name]['error']}")

        print(f"\n📈 成功率: {found_count}/{total_count} ({found_count/total_count*100:.1f}%)")

        # 次のステップ
        print("\n" + "="*60)
        print("🎯 次のステップ")
        print("="*60)

        if found_count > 0:
            print(f"\n✅ 発見したRSS URLをnews_collector.pyに追加:")
            print("```python")
            for name, result in results.items():
                if result['found'] and result['rss_urls']:
                    # 最初のURLを使用
                    rss_url = result['rss_urls'][0]
                    print(f"'{name}': {{")
                    print(f"    'rss_url': '{rss_url}',")
                    print(f"    'country': '国コード',  # 要設定")
                    print(f"    'country_emoji': '国旗絵文字',  # 要設定")
                    print(f"    'country_name_ja': '日本語国名',  # 要設定")
                    print(f"    'description': 'メーカー特徴'  # 要設定")
                    print(f"}},")
            print("```")

        if not_found:
            print(f"\n⚠️  未発見のメーカーはスクレイピングを検討:")
            for name in not_found:
                print(f"   • {name}")


def main():
    """メイン処理"""
    discovery = RSSDiscovery()

    print("🔍 自動車メーカー RSS URL 自動探索ツール")
    print("="*60)
    print()

    # 全メーカーを探索
    results = discovery.discover_all()

    # サマリーを表示
    discovery.print_summary(results)

    print("\n✨ 探索完了")


if __name__ == "__main__":
    main()
