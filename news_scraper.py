#!/usr/bin/env python3
"""
News Scraper for Automobile Manufacturers

robots.txt許可済みのメーカーニュースルームから記事をスクレイピング
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Optional
from datetime import datetime
import time
import re


class NewsScraper:
    """ニュース記事をスクレイピングするクラス"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        })

        # スクレイピング対象メーカーの設定
        self.scraping_configs = {
            'Mercedes-Benz': {
                'url': 'https://media.mercedes-benz.com/news',
                'article_selector': 'article.news-item, div.news-item, div.article-item',
                'title_selector': 'h2, h3, .title, .headline',
                'link_selector': 'a',
                'date_selector': 'time, .date, .published',
                'summary_selector': 'p, .summary, .description',
                'max_articles': 20
            },
            'Audi': {
                'url': 'https://www.audi-mediacenter.com/en/press-releases',
                'article_selector': 'li.detailed-page-list-item',
                'title_selector': 'a',
                'link_selector': 'a',
                'date_selector': 'time, .date, span.date',
                'summary_selector': 'p, .teaser, .summary',
                'max_articles': 20
            },
            'Volkswagen': {
                'url': 'https://www.volkswagen-newsroom.com/en/press-releases',
                'article_selector': 'h3.page-preview--title',
                'title_selector': 'a',
                'link_selector': 'a',
                'date_selector': 'time, .date',
                'summary_selector': 'p, .summary',
                'max_articles': 20
            },
            'Jaguar': {
                'url': 'https://media.jaguar.com/news',
                'article_selector': 'article, div.news-item',
                'title_selector': 'h2, h3, .title',
                'link_selector': 'a',
                'date_selector': 'time, .date',
                'summary_selector': 'p, .summary',
                'max_articles': 20
            },
            'Land Rover': {
                'url': 'https://media.landrover.com/news',
                'article_selector': 'article, div.news-item',
                'title_selector': 'h2, h3, .title',
                'link_selector': 'a',
                'date_selector': 'time, .date',
                'summary_selector': 'p, .summary',
                'max_articles': 20
            },
        }

    def analyze_html_structure(self, manufacturer: str) -> Dict:
        """
        メーカーのニュースページのHTML構造を分析

        Args:
            manufacturer: メーカー名

        Returns:
            分析結果の辞書
        """
        if manufacturer not in self.scraping_configs:
            return {'error': f'{manufacturer} is not in scraping configs'}

        config = self.scraping_configs[manufacturer]
        url = config['url']

        print(f"\n{'='*60}")
        print(f"🔍 {manufacturer} のHTML構造を分析中...")
        print(f"   URL: {url}")
        print(f"{'='*60}\n")

        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # 一般的な記事コンテナのパターンを探索
            potential_selectors = [
                'article',
                'div.news-item',
                'div.press-release',
                'div.article-item',
                'div[class*="news"]',
                'div[class*="article"]',
                'li.news-item',
                'div[class*="press"]',
            ]

            found_elements = {}
            for selector in potential_selectors:
                elements = soup.select(selector)
                if elements:
                    found_elements[selector] = len(elements)
                    print(f"✅ 発見: '{selector}' - {len(elements)}個")

            # タイトル要素の分析
            print(f"\n📰 タイトル要素を探索中...")
            title_selectors = ['h1', 'h2', 'h3', '.title', '.headline', 'a.title']
            for selector in title_selectors:
                titles = soup.select(selector)
                if titles:
                    print(f"   '{selector}' - {len(titles)}個")
                    if len(titles) > 0 and len(titles) < 50:  # 記事タイトルとして妥当な数
                        print(f"      例: {titles[0].get_text(strip=True)[:60]}...")

            # 日付要素の分析
            print(f"\n📅 日付要素を探索中...")
            date_selectors = ['time', '.date', '.published', 'span.date', '[datetime]']
            for selector in date_selectors:
                dates = soup.select(selector)
                if dates:
                    print(f"   '{selector}' - {len(dates)}個")
                    if dates:
                        print(f"      例: {dates[0].get_text(strip=True)[:40]}")

            # リンク要素の分析
            print(f"\n🔗 リンク構造を分析中...")
            all_links = soup.find_all('a', href=True)
            news_links = [a for a in all_links if any(
                keyword in a.get('href', '').lower()
                for keyword in ['news', 'press', 'release', 'article']
            )]
            print(f"   全リンク: {len(all_links)}個")
            print(f"   ニュース関連リンク: {len(news_links)}個")

            return {
                'manufacturer': manufacturer,
                'url': url,
                'found_selectors': found_elements,
                'total_links': len(all_links),
                'news_links': len(news_links),
                'status': 'success'
            }

        except Exception as e:
            print(f"❌ エラー: {str(e)}")
            return {
                'manufacturer': manufacturer,
                'url': url,
                'error': str(e),
                'status': 'failed'
            }

    def scrape_news(self, manufacturer: str, hours_back: int = 48) -> List[Dict]:
        """
        特定メーカーのニュースをスクレイピング

        Args:
            manufacturer: メーカー名
            hours_back: 何時間前までの記事を取得するか

        Returns:
            記事のリスト
        """
        if manufacturer not in self.scraping_configs:
            print(f"⚠️  {manufacturer} はスクレイピング設定がありません")
            return []

        config = self.scraping_configs[manufacturer]
        url = config['url']

        print(f"🌐 {manufacturer} からスクレイピング中... ({url})")

        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # 記事コンテナを検索
            articles = soup.select(config['article_selector'])

            if not articles:
                print(f"   ⚠️  記事が見つかりませんでした（セレクタ: {config['article_selector']}）")
                return []

            print(f"   📰 {len(articles)} 件の記事候補を発見")

            scraped_articles = []

            for i, article in enumerate(articles[:config['max_articles']], 1):
                try:
                    # タイトルを取得
                    title_elem = article.select_one(config['title_selector'])
                    if not title_elem:
                        continue
                    title = title_elem.get_text(strip=True)

                    # リンクを取得
                    link_elem = article.select_one(config['link_selector'])
                    if not link_elem or not link_elem.get('href'):
                        continue
                    link = urljoin(url, link_elem.get('href'))

                    # 要約を取得
                    summary_elem = article.select_one(config['summary_selector'])
                    summary = summary_elem.get_text(strip=True)[:500] if summary_elem else ''

                    # 日付を取得（オプション）
                    date_elem = article.select_one(config['date_selector'])
                    pub_date = datetime.now().isoformat()  # デフォルトは現在時刻
                    if date_elem:
                        date_text = date_elem.get_text(strip=True)
                        # 日付パースは後で実装可能
                        pub_date = datetime.now().isoformat()

                    article_data = {
                        'title': title,
                        'url': link,
                        'summary': summary,
                        'published': pub_date,
                        'source': manufacturer,
                        'category': 'car',
                        'scraping': True  # スクレイピングで取得したことを示すフラグ
                    }

                    scraped_articles.append(article_data)

                except Exception as e:
                    print(f"      ⚠️  記事{i}の処理中にエラー: {str(e)[:50]}")
                    continue

            print(f"   ✅ {len(scraped_articles)} 件の記事を取得完了")

            # レート制限（2-3秒待機）
            time.sleep(2.5)

            return scraped_articles

        except Exception as e:
            print(f"   ❌ スクレイピング失敗: {str(e)}")
            return []

    def scrape_all(self, hours_back: int = 48) -> Dict[str, List[Dict]]:
        """
        全メーカーのニュースをスクレイピング

        Args:
            hours_back: 何時間前までの記事を取得するか

        Returns:
            メーカー名をキーとした記事リストの辞書
        """
        print(f"\n🚀 スクレイピング開始（対象: {len(self.scraping_configs)} 社）\n")

        results = {}

        for manufacturer in self.scraping_configs.keys():
            articles = self.scrape_news(manufacturer, hours_back)
            results[manufacturer] = articles

        total_articles = sum(len(articles) for articles in results.values())
        print(f"\n✅ スクレイピング完了: 合計 {total_articles} 件の記事を取得\n")

        return results


def main():
    """メイン処理: HTML構造分析"""
    scraper = NewsScraper()

    print("🔍 自動車メーカー HTML構造分析ツール")
    print("="*60)
    print()

    # 全メーカーのHTML構造を分析
    for manufacturer in scraper.scraping_configs.keys():
        result = scraper.analyze_html_structure(manufacturer)
        time.sleep(3)  # レート制限

    print("\n" + "="*60)
    print("✨ 分析完了")
    print("="*60)


if __name__ == "__main__":
    main()
