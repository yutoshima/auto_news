import feedparser
from datetime import datetime, timedelta
from typing import List, Dict
import time

class NewsCollector:
    """RSSフィードからニュースを収集するクラス"""

    def __init__(self):
        # 車関連ニュースサイト
        self.car_feeds = {
            'Car Watch': 'https://car.watch.impress.co.jp/data/rss/1.0/cw/feed.rdf',
            'Response': 'https://response.jp/rss/index.rdf',
            'Autoblog Japan': 'https://jp.autoblog.com/rss.xml',
        }

        # IT関連ニュースサイト
        self.it_feeds = {
            'ITmedia News': 'https://www.itmedia.co.jp/news/rss/rss2.xml',
            'ITmedia AI+': 'https://rss.itmedia.co.jp/rss/2.0/aiplus.xml',
            '@IT': 'https://rss.itmedia.co.jp/rss/2.0/ait.xml',
            'Publickey': 'https://www.publickey1.jp/atom.xml',
            'GIZMODO Japan': 'https://www.gizmodo.jp/index.xml',
            'TechCrunch Japan': 'https://techcrunch.com/feed/',
            'Engadget日本版': 'https://japanese.engadget.com/rss.xml',
            'CNET Japan': 'https://japan.cnet.com/rss/index.rdf',
            'Zenn': 'https://zenn.dev/feed',
            'Qiita (JavaScript)': 'https://qiita.com/tags/JavaScript/feed.atom',
            'Qiita (Python)': 'https://qiita.com/tags/Python/feed.atom',
            'Qiita (React)': 'https://qiita.com/tags/React/feed.atom',
        }

        # すべてのフィードを統合（後方互換性のため）
        self.rss_feeds = {**self.car_feeds, **self.it_feeds}

        # グローバル自動車メーカーの公式RSS
        self.manufacturer_feeds = {
            'Toyota Global': 'https://global.toyota/en/newsroom/rss/',
            'Honda': 'https://global.honda/en/newsroom/rss/news.xml',
            'Tesla': 'https://www.tesla.com/blog/rss',
        }

    def fetch_recent_news(self, hours_back: int = 24) -> List[Dict]:
        """
        過去N時間以内のニュース記事を取得

        Args:
            hours_back: 何時間前までの記事を取得するか

        Returns:
            記事のリスト（カテゴリ情報を含む）
        """
        articles = []
        cutoff_time = datetime.now() - timedelta(hours=hours_back)

        # 車関連記事を取得
        for source_name, feed_url in self.car_feeds.items():
            articles.extend(self._fetch_from_feed(source_name, feed_url, cutoff_time, 'car'))

        # IT関連記事を取得
        for source_name, feed_url in self.it_feeds.items():
            articles.extend(self._fetch_from_feed(source_name, feed_url, cutoff_time, 'it'))

        # メーカー公式記事を取得（車カテゴリ）
        for source_name, feed_url in self.manufacturer_feeds.items():
            articles.extend(self._fetch_from_feed(source_name, feed_url, cutoff_time, 'car'))

        # 公開日時順にソート
        articles.sort(key=lambda x: x['published'], reverse=True)

        print(f"\n✅ 合計 {len(articles)} 件の記事を取得しました")
        print(f"   - 車: {len([a for a in articles if a['category'] == 'car'])} 件")
        print(f"   - IT: {len([a for a in articles if a['category'] == 'it'])} 件\n")

        return articles

    def _fetch_from_feed(self, source_name: str, feed_url: str, cutoff_time: datetime, category: str) -> List[Dict]:
        """
        単一のRSSフィードから記事を取得

        Args:
            source_name: 情報源名
            feed_url: RSSフィードのURL
            cutoff_time: この日時より新しい記事のみ取得
            category: 'car' または 'it'

        Returns:
            記事のリスト
        """
        articles = []

        try:
            print(f"📡 {source_name} ({category}) から取得中...")
            feed = feedparser.parse(feed_url)

            for entry in feed.entries:
                try:
                    # 公開日時の取得（フィード形式により異なる）
                    if hasattr(entry, 'published_parsed') and entry.published_parsed:
                        pub_date = datetime(*entry.published_parsed[:6])
                    elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                        pub_date = datetime(*entry.updated_parsed[:6])
                    else:
                        pub_date = datetime.now()

                    # 指定時間内の記事のみ追加
                    if pub_date >= cutoff_time:
                        article = {
                            'title': entry.title,
                            'url': entry.link,
                            'summary': entry.get('summary', entry.get('description', ''))[:500],
                            'published': pub_date.isoformat(),
                            'source': source_name,
                            'category': category,
                        }
                        articles.append(article)

                except Exception as e:
                    print(f"  ⚠️  記事の処理中にエラー: {str(e)[:50]}")
                    continue

            # レート制限対策（少し待機）
            time.sleep(0.5)

        except Exception as e:
            print(f"  ❌ {source_name} の取得に失敗: {str(e)[:50]}")

        return articles

    def get_manufacturer_news_only(self, hours_back: int = 48) -> List[Dict]:
        """
        メーカー公式の新型車情報のみを取得（より長い期間）

        Args:
            hours_back: 何時間前までの記事を取得するか（デフォルト48時間）

        Returns:
            記事のリスト
        """
        articles = []
        cutoff_time = datetime.now() - timedelta(hours=hours_back)

        for source_name, feed_url in self.manufacturer_feeds.items():
            try:
                print(f"🏭 {source_name} 公式情報を取得中...")
                feed = feedparser.parse(feed_url)

                for entry in feed.entries:
                    try:
                        if hasattr(entry, 'published_parsed') and entry.published_parsed:
                            pub_date = datetime(*entry.published_parsed[:6])
                        else:
                            pub_date = datetime.now()

                        if pub_date >= cutoff_time:
                            article = {
                                'title': entry.title,
                                'url': entry.link,
                                'summary': entry.get('summary', entry.get('description', ''))[:500],
                                'published': pub_date.isoformat(),
                                'source': source_name,
                            }
                            articles.append(article)

                    except Exception as e:
                        continue

                time.sleep(0.5)

            except Exception as e:
                print(f"  ❌ {source_name} の取得に失敗: {str(e)[:50]}")
                continue

        return articles
