# ニュースルームスクレイピング機能 - 実装提案

## 概要

RSS配信がないメーカーのニュースルームから直接記事情報を取得する機能を追加します。

---

## 法律的考慮事項

### ✅ 合法的な利用条件

1. **公開情報のみ取得**
   - ログインや認証が不要な公開ページのみ
   - 誰でもアクセス可能な情報

2. **robots.txtの尊重**
   - 各サイトのrobots.txtを確認
   - クロール禁止のパスは回避

3. **利用規約の確認**
   - 各メーカーサイトの利用規約を確認
   - スクレイピング禁止の記載がないことを確認

4. **適切なレート制限**
   - 各サイトへのアクセスは最低2-3秒間隔
   - サーバー負荷を最小限に

5. **User-Agentの設定**
   - 身元を明示するUser-Agent
   - 例: "AutoNewsBot/1.0 (Educational Purpose)"

6. **データの利用範囲**
   - 個人的なニュース配信用途のみ
   - 営利目的での利用は避ける
   - 元記事へのリンクを必ず含める

### ⚠️ 注意事項

- **著作権**: タイトルと概要のみ取得、全文コピーは避ける
- **頻度**: 1日1-2回程度の取得に制限
- **エラーハンドリング**: サイト構造変更時のエラー対応

---

## 技術実装

### 必要なライブラリ

```bash
pip install beautifulsoup4 requests lxml
# または Selenium を使う場合
pip install selenium webdriver-manager
```

### 実装例: news_scraper.py

```python
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from datetime import datetime
import time
import urllib.robotparser
from urllib.parse import urljoin, urlparse

class NewsScraper:
    """ニュースルームから記事をスクレイピングするクラス"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AutoNewsBot/1.0 (Educational Purpose; Contact: your-email@example.com)',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8',
        })

        # スクレイピング設定（RSS非対応メーカー用）
        self.scraping_configs = {
            'Nissan': {
                'url': 'https://global.nissannews.com/en/releases',
                'selectors': {
                    'article': 'div.release-item',
                    'title': 'h3.release-title',
                    'link': 'a.release-link',
                    'date': 'span.release-date',
                    'summary': 'p.release-summary'
                }
            },
            'Mercedes-Benz': {
                'url': 'https://media.mercedes-benz.com/news',
                'selectors': {
                    'article': 'article.news-item',
                    'title': 'h2.news-title',
                    'link': 'a.news-link',
                    'date': 'time.news-date',
                    'summary': 'div.news-teaser'
                }
            },
            # 他のメーカーも同様に追加
        }

    def check_robots_txt(self, base_url: str, path: str) -> bool:
        """
        robots.txtを確認してクロール可能かチェック

        Args:
            base_url: ベースURL（例: https://example.com）
            path: チェックするパス（例: /news）

        Returns:
            クロール可能ならTrue
        """
        try:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(urljoin(base_url, '/robots.txt'))
            rp.read()

            user_agent = self.session.headers['User-Agent']
            return rp.can_fetch(user_agent, urljoin(base_url, path))
        except Exception as e:
            print(f"⚠️  robots.txt確認エラー: {e}")
            # エラー時は安全のためFalseを返す
            return False

    def scrape_newsroom(self, manufacturer: str, config: Dict) -> List[Dict]:
        """
        ニュースルームから記事を取得

        Args:
            manufacturer: メーカー名
            config: スクレイピング設定

        Returns:
            記事のリスト
        """
        articles = []
        url = config['url']

        try:
            # robots.txtチェック
            parsed_url = urlparse(url)
            base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

            if not self.check_robots_txt(base_url, parsed_url.path):
                print(f"⚠️  {manufacturer}: robots.txtによりクロール禁止")
                return []

            print(f"🌐 {manufacturer} のニュースルームをスクレイピング中...")

            # ページ取得（タイムアウト設定）
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            # Beautiful Soupでパース
            soup = BeautifulSoup(response.content, 'lxml')

            # 記事要素を取得
            selectors = config['selectors']
            article_elements = soup.select(selectors['article'])

            for element in article_elements[:10]:  # 最新10件まで
                try:
                    # タイトル取得
                    title_elem = element.select_one(selectors['title'])
                    if not title_elem:
                        continue
                    title = title_elem.get_text(strip=True)

                    # リンク取得
                    link_elem = element.select_one(selectors['link'])
                    if not link_elem:
                        continue
                    link = link_elem.get('href')
                    if not link.startswith('http'):
                        link = urljoin(base_url, link)

                    # 日付取得
                    date_elem = element.select_one(selectors.get('date'))
                    pub_date = datetime.now()
                    if date_elem:
                        date_text = date_elem.get_text(strip=True)
                        # 日付パース（形式は要調整）
                        try:
                            pub_date = datetime.strptime(date_text, '%Y-%m-%d')
                        except:
                            pass

                    # 概要取得
                    summary_elem = element.select_one(selectors.get('summary', ''))
                    summary = summary_elem.get_text(strip=True) if summary_elem else ''

                    article = {
                        'title': title,
                        'url': link,
                        'summary': summary[:500],
                        'published': pub_date.isoformat(),
                        'source': manufacturer,
                        'category': 'car',
                        'method': 'scraping'  # スクレイピングで取得したことを明示
                    }

                    articles.append(article)

                except Exception as e:
                    print(f"  ⚠️  記事の処理中にエラー: {str(e)[:50]}")
                    continue

            print(f"  ✅ {len(articles)} 件の記事を取得")

            # レート制限（重要）
            time.sleep(3)  # 3秒待機

        except requests.RequestException as e:
            print(f"  ❌ {manufacturer} の取得に失敗: {str(e)[:50]}")
        except Exception as e:
            print(f"  ❌ {manufacturer} の処理中にエラー: {str(e)[:50]}")

        return articles

    def fetch_all_scraped_news(self, hours_back: int = 168) -> List[Dict]:
        """
        全メーカーのニュースルームから記事を取得

        Args:
            hours_back: 何時間前までの記事を対象とするか

        Returns:
            記事のリスト
        """
        all_articles = []

        for manufacturer, config in self.scraping_configs.items():
            articles = self.scrape_newsroom(manufacturer, config)
            all_articles.extend(articles)

        return all_articles
```

### news_collector.pyへの統合

```python
from news_scraper import NewsScraper

class NewsCollector:
    def __init__(self):
        # 既存のコード...

        # スクレイパーを追加
        self.scraper = NewsScraper()

    def fetch_recent_news(self, hours_back: int = 24, use_scraping: bool = False) -> List[Dict]:
        """
        過去N時間以内のニュース記事を取得

        Args:
            hours_back: 何時間前までの記事を取得するか
            use_scraping: スクレイピングを使用するか（デフォルト: False）
        """
        articles = []
        cutoff_time = datetime.now() - timedelta(hours=hours_back)

        # IT記事取得
        for source_name, feed_url in self.it_feeds.items():
            articles.extend(self._fetch_from_feed(source_name, feed_url, cutoff_time, 'it'))

        # メーカー公式RSS取得
        for manufacturer_name, manufacturer_info in self.manufacturer_feeds.items():
            feed_url = manufacturer_info['rss_url']
            articles.extend(self._fetch_from_feed(
                manufacturer_name,
                feed_url,
                cutoff_time,
                'car',
                manufacturer_info=manufacturer_info
            ))

        # スクレイピング取得（オプション）
        if use_scraping:
            print("\n🌐 スクレイピングでニュース取得を開始...")
            scraped_articles = self.scraper.fetch_all_scraped_news(hours_back)
            articles.extend(scraped_articles)

        # 公開日時順にソート
        articles.sort(key=lambda x: x['published'], reverse=True)

        return articles
```

---

## 対象メーカー（スクレイピング候補）

### RSS未確認のメーカー

1. **🇯🇵 Nissan**
   - URL: https://global.nissannews.com/en/releases
   - 難易度: ⭐⭐☆☆☆（比較的簡単）

2. **🇩🇪 Mercedes-Benz**
   - URL: https://media.mercedes-benz.com/news
   - 難易度: ⭐⭐⭐☆☆（中程度）

3. **🇩🇪 BMW**
   - URL: https://www.press.bmwgroup.com/global/article/
   - 難易度: ⭐⭐⭐☆☆（中程度）

4. **🇩🇪 Audi**
   - URL: https://www.audi-mediacenter.com/en/press-releases
   - 難易度: ⭐⭐⭐☆☆（中程度）

5. **🇺🇸 Chevrolet / Cadillac**
   - URL: https://media.chevrolet.com/media/us/en/chevrolet/news.html
   - 難易度: ⭐⭐☆☆☆（比較的簡単）

---

## 段階的実装計画

### Phase 1: 調査（1-2日）
- [ ] 各メーカーのrobots.txtを確認
- [ ] 利用規約を確認
- [ ] ニュースページのHTML構造を分析
- [ ] セレクタパターンを特定

### Phase 2: プロトタイプ（2-3日）
- [ ] NewScraperクラスの実装
- [ ] 1-2メーカーでテスト
- [ ] エラーハンドリングの実装
- [ ] レート制限の実装

### Phase 3: 統合（1-2日）
- [ ] news_collector.pyへの統合
- [ ] コマンドラインオプション追加
- [ ] ログ出力の整備
- [ ] テスト実行

### Phase 4: 検証（1-2日）
- [ ] 全メーカーでの動作確認
- [ ] 取得データの品質チェック
- [ ] パフォーマンス測定
- [ ] ドキュメント作成

---

## コマンドライン使用例

```bash
# スクレイピングを有効にして実行
python main.py --mode new-cars --hours 168 --use-scraping

# スクレイピングのみテスト
python main.py --mode test-scraping
```

---

## リスクと対策

### リスク1: サイト構造の変更
**対策:**
- 定期的な動作確認
- エラー通知機能
- フォールバック機能（RSS優先）

### リスク2: アクセス制限
**対策:**
- 適切なレート制限
- User-Agent設定
- タイムアウト設定

### リスク3: 法的問題
**対策:**
- robots.txt遵守
- 利用規約確認
- 個人利用範囲の明示

### リスク4: メンテナンスコスト
**対策:**
- 詳細なドキュメント
- セレクタ設定の外部化（YAML/JSONファイル）
- エラーログの充実

---

## 推奨事項

### ✅ DO（推奨）
1. **RSS優先** - RSSがある場合は必ずRSSを使う
2. **レート制限** - 各サイト最低2-3秒の間隔
3. **robots.txt遵守** - 必ずチェックする
4. **エラーハンドリング** - 失敗しても他のメーカーは継続
5. **ログ記録** - 取得状況を詳細に記録

### ❌ DON'T（非推奨）
1. **高頻度アクセス** - 1日1-2回まで
2. **全文コピー** - タイトルと概要のみ
3. **認証突破** - ログインページは対象外
4. **User-Agent偽装** - 正直に身元を明示

---

## 次のステップ

このスクレイピング機能を実装する場合：

1. **調査フェーズ**
   - 各メーカーのrobots.txtとHTML構造を調査
   - セレクタパターンをドキュメント化

2. **実装フェーズ**
   - `news_scraper.py` を作成
   - テストコード作成
   - 統合とテスト

3. **運用フェーズ**
   - 定期的な動作確認
   - エラー監視
   - 必要に応じてメンテナンス

---

## 結論

**スクレイピングは技術的・法律的に可能ですが、以下の条件付きで推奨します：**

✅ **推奨する場合:**
- RSSが本当に存在しない
- 個人利用・教育目的
- 適切なレート制限を設定
- robots.txtを遵守

⚠️ **慎重に検討すべき場合:**
- 商用利用
- 大量データ取得
- 高頻度アクセス

📝 **実装したい場合は:**
1. まず各メーカーのrobots.txtと利用規約を確認
2. 1-2メーカーでプロトタイプ実装
3. 問題なければ段階的に拡大

**実装を進めますか？その場合は調査フェーズから始めることを推奨します。**
