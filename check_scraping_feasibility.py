#!/usr/bin/env python3
"""
スクレイピング可否確認ツール

各メーカーのニュースルームがスクレイピング可能か確認します：
- robots.txtの確認
- ページアクセス確認
- HTML構造の確認
"""

import requests
import urllib.robotparser
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time

class ScrapingChecker:
    """スクレイピング可否をチェックするクラス"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AutoNewsBot/1.0 (Educational Purpose; Checking Scraping Feasibility)',
            'Accept': 'text/html,application/xhtml+xml',
        })

        # チェック対象のメーカー
        self.manufacturers = {
            'Nissan': 'https://global.nissannews.com/en/releases',
            'Mercedes-Benz': 'https://media.mercedes-benz.com/news',
            'BMW': 'https://www.press.bmwgroup.com/global/article/detail',
            'Audi': 'https://www.audi-mediacenter.com/en/press-releases',
            'Volkswagen': 'https://www.volkswagen-newsroom.com/en/press-releases',
            'Chevrolet': 'https://media.chevrolet.com/media/us/en/chevrolet/news.html',
            'Cadillac': 'https://media.cadillac.com/media/us/en/cadillac/news.html',
            'Jaguar': 'https://media.jaguarlandrover.com/news',
            'Land Rover': 'https://media.jaguarlandrover.com/news',
            'Volvo': 'https://www.media.volvocars.com/global/en-gb/media/pressreleases',
        }

    def check_robots_txt(self, base_url: str, path: str) -> dict:
        """
        robots.txtを確認

        Returns:
            {
                'allowed': bool,
                'robots_url': str,
                'content': str or None
            }
        """
        result = {
            'allowed': False,
            'robots_url': urljoin(base_url, '/robots.txt'),
            'content': None,
            'error': None
        }

        try:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(result['robots_url'])
            rp.read()

            user_agent = self.session.headers['User-Agent']
            result['allowed'] = rp.can_fetch(user_agent, urljoin(base_url, path))

            # robots.txtの内容を取得
            try:
                robots_response = requests.get(result['robots_url'], timeout=5)
                if robots_response.status_code == 200:
                    result['content'] = robots_response.text[:500]  # 最初の500文字
            except:
                pass

        except Exception as e:
            result['error'] = str(e)
            result['allowed'] = False  # エラー時は安全のためFalse

        return result

    def check_page_access(self, url: str) -> dict:
        """
        ページにアクセス可能か確認

        Returns:
            {
                'accessible': bool,
                'status_code': int or None,
                'error': str or None
            }
        """
        result = {
            'accessible': False,
            'status_code': None,
            'error': None,
            'has_articles': False
        }

        try:
            response = self.session.get(url, timeout=10)
            result['status_code'] = response.status_code
            result['accessible'] = response.status_code == 200

            if result['accessible']:
                # 簡易的な記事要素チェック
                soup = BeautifulSoup(response.content, 'html.parser')

                # よくある記事コンテナのパターン
                article_patterns = [
                    'article', 'div.news', 'div.press-release',
                    'div.release', 'li.news-item', 'div.story'
                ]

                for pattern in article_patterns:
                    elements = soup.select(pattern)
                    if len(elements) > 0:
                        result['has_articles'] = True
                        result['article_count'] = len(elements)
                        result['article_pattern'] = pattern
                        break

        except requests.RequestException as e:
            result['error'] = str(e)
        except Exception as e:
            result['error'] = f"Unexpected error: {str(e)}"

        return result

    def check_manufacturer(self, name: str, url: str) -> dict:
        """
        特定のメーカーをチェック

        Returns:
            総合的なチェック結果
        """
        print(f"\n{'='*60}")
        print(f"🔍 {name} をチェック中...")
        print(f"   URL: {url}")

        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        # robots.txtチェック
        print(f"\n📄 robots.txt を確認中...")
        robots_result = self.check_robots_txt(base_url, parsed_url.path)

        if robots_result['allowed']:
            print(f"   ✅ クロール許可")
        else:
            print(f"   ❌ クロール禁止")
            if robots_result['error']:
                print(f"   ⚠️  エラー: {robots_result['error']}")

        if robots_result['content']:
            print(f"   📝 robots.txt (抜粋):")
            for line in robots_result['content'].split('\n')[:5]:
                if line.strip():
                    print(f"      {line}")

        # ページアクセスチェック
        print(f"\n🌐 ページアクセスを確認中...")
        access_result = self.check_page_access(url)

        if access_result['accessible']:
            print(f"   ✅ アクセス可能 (Status: {access_result['status_code']})")
            if access_result['has_articles']:
                print(f"   📰 記事要素を発見: {access_result.get('article_count', 0)} 件")
                print(f"   🎯 パターン: {access_result.get('article_pattern', 'N/A')}")
            else:
                print(f"   ⚠️  記事要素が見つかりませんでした")
        else:
            print(f"   ❌ アクセス不可")
            if access_result['error']:
                print(f"   ⚠️  エラー: {access_result['error']}")

        # 総合判定
        feasible = robots_result['allowed'] and access_result['accessible']

        print(f"\n{'─'*60}")
        if feasible:
            print(f"✅ {name}: スクレイピング可能")
            if access_result['has_articles']:
                print(f"   推奨度: ⭐⭐⭐ (記事要素が検出されました)")
            else:
                print(f"   推奨度: ⭐⭐☆ (HTML構造の詳細調査が必要)")
        else:
            print(f"❌ {name}: スクレイピング非推奨")
            if not robots_result['allowed']:
                print(f"   理由: robots.txtで禁止されています")
            if not access_result['accessible']:
                print(f"   理由: ページにアクセスできません")

        # レート制限対策
        time.sleep(2)

        return {
            'name': name,
            'url': url,
            'feasible': feasible,
            'robots': robots_result,
            'access': access_result
        }

    def check_all(self) -> list:
        """全メーカーをチェック"""
        print("🚀 スクレイピング可否チェックを開始します")
        print(f"対象メーカー: {len(self.manufacturers)} 社\n")

        results = []

        for name, url in self.manufacturers.items():
            result = self.check_manufacturer(name, url)
            results.append(result)

        return results

    def print_summary(self, results: list):
        """チェック結果のサマリーを表示"""
        print("\n" + "="*60)
        print("📊 チェック結果サマリー")
        print("="*60)

        feasible = [r for r in results if r['feasible']]
        not_feasible = [r for r in results if not r['feasible']]

        print(f"\n✅ スクレイピング可能: {len(feasible)} 社")
        for r in feasible:
            has_articles = r['access'].get('has_articles', False)
            star = "⭐⭐⭐" if has_articles else "⭐⭐☆"
            print(f"   {star} {r['name']}")

        print(f"\n❌ スクレイピング非推奨: {len(not_feasible)} 社")
        for r in not_feasible:
            print(f"   • {r['name']}")

        print(f"\n📈 成功率: {len(feasible)}/{len(results)} ({len(feasible)/len(results)*100:.1f}%)")

        print("\n" + "="*60)
        print("🎯 推奨事項")
        print("="*60)

        if feasible:
            print("\n✅ 以下のメーカーはスクレイピング可能です：")
            for r in feasible:
                print(f"\n   【{r['name']}】")
                print(f"   URL: {r['url']}")
                if r['access'].get('has_articles'):
                    print(f"   パターン: {r['access'].get('article_pattern')}")
                    print(f"   記事数: {r['access'].get('article_count')} 件")
                print(f"   次のステップ: HTML構造の詳細分析")

        if not_feasible:
            print("\n⚠️  以下のメーカーは代替手段を検討してください：")
            for r in not_feasible:
                print(f"\n   【{r['name']}】")
                if not r['robots']['allowed']:
                    print(f"   問題: robots.txtで禁止")
                    print(f"   代替案: 公式RSS / 公式API を探す")
                if not r['access']['accessible']:
                    print(f"   問題: ページアクセス不可")
                    print(f"   代替案: URL を確認、または別のニュースページを探す")


def main():
    """メイン処理"""
    checker = ScrapingChecker()

    print("🤖 自動車メーカー ニュースルーム スクレイピング可否チェックツール")
    print("="*60)
    print()

    # 全メーカーをチェック
    results = checker.check_all()

    # サマリーを表示
    checker.print_summary(results)

    print("\n✨ チェック完了")


if __name__ == "__main__":
    main()
