import feedparser
from datetime import datetime, timedelta
from typing import List, Dict
import time

class NewsCollector:
    """RSSフィードからニュースを収集するクラス"""

    def __init__(self):
        # IT関連ニュースサイト（日本語 + 英語）
        self.it_feeds = {
            # 🇯🇵 日本語メディア
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

            # 🌍 グローバルメディア（英語 → 自動翻訳）
            'The Verge': 'https://www.theverge.com/rss/index.xml',
            'Hacker News': 'https://news.ycombinator.com/rss',

            # ☁️ クラウド・インフラ公式（英語 → 自動翻訳）
            'AWS What\'s New': 'https://aws.amazon.com/about-aws/whats-new/recent/feed/',
            'Microsoft DevBlogs': 'https://devblogs.microsoft.com/feed/',
            'GitHub Blog': 'https://github.blog/feed/',

            # 🤖 AI企業公式（英語 → 自動翻訳）
            'OpenAI Blog': 'https://openai.com/blog/rss.xml',

            # 🔬 半導体・AIプラットフォーム（英語 → 自動翻訳）
            'NVIDIA Newsroom': 'https://nvidianews.nvidia.com/releases.xml',
        }

        # EV・自動車テックメディア（英語 → 自動翻訳）
        self.ev_tech_feeds = {
            'Electrek': 'https://electrek.co/feed/',
            'InsideEVs': 'https://insideevs.com/rss/articles/all/',
        }

        # グローバル自動車メーカーの公式RSS
        self.manufacturer_feeds = {
            # 🇯🇵 日本（5社）
            'Toyota': {
                'rss_url': 'https://global.toyota/en/newsroom/rss/',
                'country': 'japan',
                'country_emoji': '🇯🇵',
                'country_name_ja': '日本',
                'description': '世界最大の自動車メーカー、HV・EV技術のパイオニア'
            },
            'Lexus': {
                'rss_url': 'https://pressroom.lexus.com/rss',
                'country': 'japan',
                'country_emoji': '🇯🇵',
                'country_name_ja': '日本',
                'description': 'トヨタの高級ブランド、洗練されたデザインと品質'
            },
            'Honda': {
                'rss_url': 'https://www.honda.co.jp/rss/hotnews.xml',
                'country': 'japan',
                'country_emoji': '🇯🇵',
                'country_name_ja': '日本',
                'description': '技術のホンダ、二輪・四輪・航空機エンジンを展開'
            },
            'Nissan': {
                'rss_url': 'https://global.nissannews.com/rss',
                'country': 'japan',
                'country_emoji': '🇯🇵',
                'country_name_ja': '日本',
                'description': '日産・ルノー・三菱アライアンス、電動化に注力'
            },
            'Mazda': {
                'rss_url': 'https://www.mazda.com/en/rss/',
                'country': 'japan',
                'country_emoji': '🇯🇵',
                'country_name_ja': '日本',
                'description': '人馬一体の走り、独自のSKYACTIV技術とデザイン'
            },

            # 🇩🇪 ドイツ（2社）
            'Porsche': {
                'rss_url': 'https://newsroom.porsche.com/rss.xml',
                'country': 'germany',
                'country_emoji': '🇩🇪',
                'country_name_ja': 'ドイツ',
                'description': 'スポーツカーの名門、911シリーズと電動化戦略'
            },
            # 'Mercedes-Benz': {
            #     'rss_url': 'https://group-media.mercedes-benz.com/marsMediaSite/en/instance/ko/RSS-Feeds.xhtml?oid=9266299',
            #     'country': 'germany',
            #     'country_emoji': '🇩🇪',
            #     'country_name_ja': 'ドイツ',
            #     'description': '高級車の代名詞、革新的な安全技術と快適性、自動運転技術のリーダー'
            #     # 注: 2026-03-01時点でアクセス拒否エラー - 代替URL調査中
            # },
            'BMW': {
                'rss_url': 'https://www.press.bmwgroup.com/global/rss',
                'country': 'germany',
                'country_emoji': '🇩🇪',
                'country_name_ja': 'ドイツ',
                'description': '駆け抜ける歓び、スポーティな高級車メーカー'
            },
            # 'Audi': {
            #     'rss_url': 'https://www.audi-mediacenter.com/rss',  # 要確認
            #     'country': 'germany',
            #     'country_emoji': '🇩🇪',
            #     'country_name_ja': 'ドイツ',
            #     'description': 'VWグループの高級ブランド、先進技術とクアトロ'
            # },
            # 'Volkswagen': {
            #     'rss_url': 'https://www.volkswagen-newsroom.com/rss',  # 要確認
            #     'country': 'germany',
            #     'country_emoji': '🇩🇪',
            #     'country_name_ja': 'ドイツ',
            #     'description': '世界最大級の自動車グループ、大衆車から高級車'
            # },

            # 🇺🇸 アメリカ（3社）
            'General Motors': {
                'rss_url': 'https://news.gm.com/rss',
                'country': 'usa',
                'country_emoji': '🇺🇸',
                'country_name_ja': 'アメリカ',
                'description': '米国最大の自動車メーカー、シボレー・キャデラック等'
            },
            'Ford': {
                'rss_url': 'https://media.ford.com/content/fordmedia/fna/us/en/rss.html',
                'country': 'usa',
                'country_emoji': '🇺🇸',
                'country_name_ja': 'アメリカ',
                'description': '米国自動車産業の創始者、ピックアップトラックで圧倒的シェア'
            },
            'Tesla': {
                'rss_url': 'https://ir.tesla.com/rss/news-releases',
                'country': 'usa',
                'country_emoji': '🇺🇸',
                'country_name_ja': 'アメリカ',
                'description': '高級電気自動車メーカー、自動運転技術のリーダー'
            },
            # 'Chevrolet': {
            #     'rss_url': 'https://media.chevrolet.com/rss',  # 要確認
            #     'country': 'usa',
            #     'country_emoji': '🇺🇸',
            #     'country_name_ja': 'アメリカ',
            #     'description': 'GMの主力ブランド、幅広い車種ラインナップ'
            # },
            # 'Cadillac': {
            #     'rss_url': 'https://media.cadillac.com/rss',  # 要確認
            #     'country': 'usa',
            #     'country_emoji': '🇺🇸',
            #     'country_name_ja': 'アメリカ',
            #     'description': 'GMの高級ブランド、米国プレミアムカーの象徴'
            # },

            # 🇰🇷 韓国（2社）
            'Hyundai': {
                'rss_url': 'https://www.hyundainews.com/rss',
                'country': 'south_korea',
                'country_emoji': '🇰🇷',
                'country_name_ja': '韓国',
                'description': '韓国最大の自動車メーカー、デザインと品質で急成長'
            },
            'Kia': {
                'rss_url': 'https://www.kiamedia.com/us/en/rss/PressReleases/feed.rss',
                'country': 'south_korea',
                'country_emoji': '🇰🇷',
                'country_name_ja': '韓国',
                'description': 'ヒュンダイグループ、スタイリッシュなデザインとコスパ'
            },

            # 🇮🇹 イタリア（1社）
            'Lamborghini': {
                'rss_url': 'https://media.lamborghini.com/english/latest/rss',
                'country': 'italy',
                'country_emoji': '🇮🇹',
                'country_name_ja': 'イタリア',
                'description': 'スーパーカーの象徴、VWグループ傘下の超高級ブランド'
            },

            # 🇬🇧 イギリス（1社）
            'Rolls-Royce': {
                'rss_url': 'https://www.press.rolls-roycemotorcars.com/global/rss',
                'country': 'uk',
                'country_emoji': '🇬🇧',
                'country_name_ja': 'イギリス',
                'description': '超高級車の最高峰、BMWグループ傘下'
            },
            # 'Jaguar': {
            #     'rss_url': 'https://media.jaguar.com/rss',  # 要確認
            #     'country': 'uk',
            #     'country_emoji': '🇬🇧',
            #     'country_name_ja': 'イギリス',
            #     'description': '英国の高級スポーツカーメーカー、タタ傘下'
            # },
            # 'Land Rover': {
            #     'rss_url': 'https://media.landrover.com/rss',  # 要確認
            #     'country': 'uk',
            #     'country_emoji': '🇬🇧',
            #     'country_name_ja': 'イギリス',
            #     'description': '高級SUVの代表格、タタ・モーターズ傘下'
            # },

            # 🇸🇪 スウェーデン（1社）
            # 'Volvo': {
            #     'rss_url': 'https://www.media.volvocars.com/global/en-gb/rss',
            #     'country': 'sweden',
            #     'country_emoji': '🇸🇪',
            #     'country_name_ja': 'スウェーデン',
            #     'description': '安全性の代名詞、吉利汽車傘下で電動化推進、ソフトウェア定義車両（SDV）のリーダー'
            #     # 注: 2026-03-01時点でDNS障害 - 代替URL調査中
            # },
        }


    def fetch_recent_news(self, hours_back: int = 24) -> List[Dict]:
        """
        過去N時間以内のニュース記事を取得（IT + EV専門メディア + メーカー公式RSS）

        Args:
            hours_back: 何時間前までの記事を取得するか

        Returns:
            記事のリスト（カテゴリ情報を含む）
        """
        articles = []
        cutoff_time = datetime.now() - timedelta(hours=hours_back)

        # IT関連記事を取得
        for source_name, feed_url in self.it_feeds.items():
            articles.extend(self._fetch_from_feed(source_name, feed_url, cutoff_time, 'it'))

        # EV・自動車テックメディアを取得（車カテゴリ）
        for source_name, feed_url in self.ev_tech_feeds.items():
            articles.extend(self._fetch_from_feed(source_name, feed_url, cutoff_time, 'car'))

        # メーカー公式記事を取得（車カテゴリ）
        for manufacturer_name, manufacturer_info in self.manufacturer_feeds.items():
            feed_url = manufacturer_info['rss_url']
            articles.extend(self._fetch_from_feed(
                manufacturer_name,
                feed_url,
                cutoff_time,
                'car',
                manufacturer_info=manufacturer_info
            ))

        # 公開日時順にソート
        articles.sort(key=lambda x: x['published'], reverse=True)

        # カテゴリ別の統計
        car_articles = [a for a in articles if a['category'] == 'car']
        it_articles = [a for a in articles if a['category'] == 'it']

        # IT記事の内訳
        japanese_media = ['ITmedia News', 'ITmedia AI+', '@IT', 'Publickey', 'GIZMODO Japan',
                          'TechCrunch Japan', 'Engadget日本版', 'CNET Japan', 'Zenn',
                          'Qiita (JavaScript)', 'Qiita (Python)', 'Qiita (React)']
        global_media = ['The Verge', 'Hacker News']
        cloud_infra = ['AWS What\'s New', 'Microsoft DevBlogs', 'GitHub Blog']
        ai_companies = ['OpenAI Blog']
        semiconductor_ai = ['NVIDIA Newsroom']

        jp_articles = [a for a in it_articles if a['source'] in japanese_media]
        global_articles = [a for a in it_articles if a['source'] in global_media]
        cloud_articles = [a for a in it_articles if a['source'] in cloud_infra]
        ai_company_articles = [a for a in it_articles if a['source'] in ai_companies]
        semi_articles = [a for a in it_articles if a['source'] in semiconductor_ai]

        # 車記事の内訳
        ev_media_articles = [a for a in car_articles if a['source'] in self.ev_tech_feeds.keys()]
        manufacturer_articles = [a for a in car_articles if a['source'] in self.manufacturer_feeds.keys()]

        print(f"\n✅ 合計 {len(articles)} 件の記事を取得しました")
        print(f"   📱 IT: {len(it_articles)} 件")
        print(f"      ├─ 🇯🇵 日本語メディア: {len(jp_articles)} 件")
        print(f"      ├─ 🌍 グローバルメディア: {len(global_articles)} 件")
        print(f"      ├─ ☁️  クラウド・インフラ: {len(cloud_articles)} 件")
        print(f"      ├─ 🤖 AI企業公式: {len(ai_company_articles)} 件")
        print(f"      └─ 🔬 半導体・AIプラットフォーム: {len(semi_articles)} 件")
        print(f"   🚗 車: {len(car_articles)} 件")
        print(f"      ├─ ⚡ EVテックメディア: {len(ev_media_articles)} 件")
        print(f"      └─ 🏭 メーカー公式RSS: {len(manufacturer_articles)} 件\n")

        return articles

    def _fetch_from_feed(self, source_name: str, feed_url: str, cutoff_time: datetime, category: str, manufacturer_info: Dict = None) -> List[Dict]:
        """
        単一のRSSフィードから記事を取得

        Args:
            source_name: 情報源名
            feed_url: RSSフィードのURL
            cutoff_time: この日時より新しい記事のみ取得
            category: 'car' または 'it'
            manufacturer_info: メーカー情報（国、特徴など）

        Returns:
            記事のリスト
        """
        articles = []

        try:
            # メーカー情報がある場合は国旗付きで表示
            if manufacturer_info:
                print(f"📡 {manufacturer_info['country_emoji']} {source_name} ({category}) から取得中...")
            else:
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

                        # メーカー情報を記事に追加
                        if manufacturer_info:
                            article['manufacturer_info'] = {
                                'country': manufacturer_info['country'],
                                'country_emoji': manufacturer_info['country_emoji'],
                                'country_name_ja': manufacturer_info['country_name_ja'],
                                'description': manufacturer_info['description']
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
        ※ 非推奨: fetch_recent_news()が既にメーカー公式RSSのみを取得しています

        Args:
            hours_back: 何時間前までの記事を取得するか（デフォルト48時間）

        Returns:
            記事のリスト
        """
        articles = []
        cutoff_time = datetime.now() - timedelta(hours=hours_back)

        for manufacturer_name, manufacturer_info in self.manufacturer_feeds.items():
            try:
                feed_url = manufacturer_info['rss_url']
                print(f"🏭 {manufacturer_info['country_emoji']} {manufacturer_name} 公式情報を取得中...")
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
                                'source': manufacturer_name,
                                'category': 'car',
                                'manufacturer_info': {
                                    'country': manufacturer_info['country'],
                                    'country_emoji': manufacturer_info['country_emoji'],
                                    'country_name_ja': manufacturer_info['country_name_ja'],
                                    'description': manufacturer_info['description']
                                }
                            }
                            articles.append(article)

                    except Exception as e:
                        continue

                time.sleep(0.5)

            except Exception as e:
                print(f"  ❌ {manufacturer_name} の取得に失敗: {str(e)[:50]}")
                continue

        return articles
