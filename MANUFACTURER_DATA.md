# 自動車メーカー公式RSSデータ一覧

## 実装済みメーカー（15社）

### データ構造

```python
'メーカー名': {
    'rss_url': 'RSSフィードURL',
    'country': '国コード',
    'country_emoji': '国旗絵文字',
    'country_name_ja': '日本語国名',
    'description': '詳細な特徴説明（20-30文字）'
}
```

---

## 🇯🇵 日本（4社）

### 1. Toyota
```python
'Toyota': {
    'rss_url': 'https://global.toyota/en/newsroom/rss/',
    'country': 'japan',
    'country_emoji': '🇯🇵',
    'country_name_ja': '日本',
    'description': '世界最大の自動車メーカー、HV・EV技術のパイオニア'
}
```

### 2. Lexus
```python
'Lexus': {
    'rss_url': 'https://pressroom.lexus.com/rss-feeds/',
    'country': 'japan',
    'country_emoji': '🇯🇵',
    'country_name_ja': '日本',
    'description': 'トヨタの高級ブランド、洗練されたデザインと品質'
}
```

### 3. Honda
```python
'Honda': {
    'rss_url': 'https://global.honda/en/newsroom/rss/news.xml',
    'country': 'japan',
    'country_emoji': '🇯🇵',
    'country_name_ja': '日本',
    'description': '技術のホンダ、二輪・四輪・航空機エンジンを展開'
}
```

### 4. Mazda
```python
'Mazda': {
    'rss_url': 'https://www.mazda.com/en/rss/',
    'country': 'japan',
    'country_emoji': '🇯🇵',
    'country_name_ja': '日本',
    'description': '人馬一体の走り、独自のSKYACTIV技術とデザイン'
}
```

---

## 🇩🇪 ドイツ（1社）

### 5. Porsche
```python
'Porsche': {
    'rss_url': 'https://newsroom.porsche.com/rss/en/',
    'country': 'germany',
    'country_emoji': '🇩🇪',
    'country_name_ja': 'ドイツ',
    'description': 'スポーツカーの名門、911シリーズと電動化戦略'
}
```

---

## 🇺🇸 アメリカ（3社）

### 6. General Motors
```python
'General Motors': {
    'rss_url': 'https://news.gm.com/rss',
    'country': 'usa',
    'country_emoji': '🇺🇸',
    'country_name_ja': 'アメリカ',
    'description': '米国最大の自動車メーカー、シボレー・キャデラック等'
}
```

### 7. Ford
```python
'Ford': {
    'rss_url': 'https://media.ford.com/content/fordmedia/fna/us/en/rss.html',
    'country': 'usa',
    'country_emoji': '🇺🇸',
    'country_name_ja': 'アメリカ',
    'description': '米国自動車産業の創始者、ピックアップトラックで圧倒的シェア'
}
```

### 8. Tesla
```python
'Tesla': {
    'rss_url': 'https://ir.tesla.com/rss/news-releases',
    'country': 'usa',
    'country_emoji': '🇺🇸',
    'country_name_ja': 'アメリカ',
    'description': '高級電気自動車メーカー、自動運転技術のリーダー'
}
```

---

## 🇰🇷 韓国（2社）

### 9. Hyundai
```python
'Hyundai': {
    'rss_url': 'https://www.hyundainews.com/en-us/rss',
    'country': 'south_korea',
    'country_emoji': '🇰🇷',
    'country_name_ja': '韓国',
    'description': '韓国最大の自動車メーカー、デザインと品質で急成長'
}
```

### 10. Kia
```python
'Kia': {
    'rss_url': 'https://www.kiamedia.com/us/en/rss/PressReleases/feed.rss',
    'country': 'south_korea',
    'country_emoji': '🇰🇷',
    'country_name_ja': '韓国',
    'description': 'ヒュンダイグループ、スタイリッシュなデザインとコスパ'
}
```

---

## 🇮🇹 イタリア（1社）

### 11. Lamborghini
```python
'Lamborghini': {
    'rss_url': 'https://media.lamborghini.com/english/latest/rss',
    'country': 'italy',
    'country_emoji': '🇮🇹',
    'country_name_ja': 'イタリア',
    'description': 'スーパーカーの象徴、VWグループ傘下の超高級ブランド'
}
```

---

## 🇬🇧 イギリス（1社）

### 12. Rolls-Royce
```python
'Rolls-Royce': {
    'rss_url': 'https://www.press.rolls-roycemotorcars.com/rss',
    'country': 'uk',
    'country_emoji': '🇬🇧',
    'country_name_ja': 'イギリス',
    'description': '超高級車の最高峰、BMWグループ傘下'
}
```

---

## コメントアウトしたメーカー（将来追加予定）

### 🇯🇵 日本

#### Nissan
```python
# 'Nissan': {
#     'rss_url': 'https://global.nissannews.com/en/rss',  # 要確認
#     'country': 'japan',
#     'country_emoji': '🇯🇵',
#     'country_name_ja': '日本',
#     'description': '日産・ルノー・三菱アライアンス、電動化に注力'
# }
```

### 🇩🇪 ドイツ

#### Mercedes-Benz
```python
# 'Mercedes-Benz': {
#     'rss_url': 'https://media.mercedes-benz.com/rss',  # 要確認
#     'country': 'germany',
#     'country_emoji': '🇩🇪',
#     'country_name_ja': 'ドイツ',
#     'description': '高級車の代名詞、革新的な安全技術と快適性'
# }
```

#### BMW
```python
# 'BMW': {
#     'rss_url': 'https://www.press.bmwgroup.com/rss',  # 要確認
#     'country': 'germany',
#     'country_emoji': '🇩🇪',
#     'country_name_ja': 'ドイツ',
#     'description': '駆け抜ける歓び、スポーティな高級車メーカー'
# }
```

#### Audi
```python
# 'Audi': {
#     'rss_url': 'https://www.audi-mediacenter.com/rss',  # 要確認
#     'country': 'germany',
#     'country_emoji': '🇩🇪',
#     'country_name_ja': 'ドイツ',
#     'description': 'VWグループの高級ブランド、先進技術とクアトロ'
# }
```

#### Volkswagen
```python
# 'Volkswagen': {
#     'rss_url': 'https://www.volkswagen-newsroom.com/rss',  # 要確認
#     'country': 'germany',
#     'country_emoji': '🇩🇪',
#     'country_name_ja': 'ドイツ',
#     'description': '世界最大級の自動車グループ、大衆車から高級車'
# }
```

### 🇺🇸 アメリカ

#### Chevrolet
```python
# 'Chevrolet': {
#     'rss_url': 'https://media.chevrolet.com/rss',  # 要確認
#     'country': 'usa',
#     'country_emoji': '🇺🇸',
#     'country_name_ja': 'アメリカ',
#     'description': 'GMの主力ブランド、幅広い車種ラインナップ'
# }
```

#### Cadillac
```python
# 'Cadillac': {
#     'rss_url': 'https://media.cadillac.com/rss',  # 要確認
#     'country': 'usa',
#     'country_emoji': '🇺🇸',
#     'country_name_ja': 'アメリカ',
#     'description': 'GMの高級ブランド、米国プレミアムカーの象徴'
# }
```

### 🇬🇧 イギリス

#### Jaguar
```python
# 'Jaguar': {
#     'rss_url': 'https://media.jaguar.com/rss',  # 要確認
#     'country': 'uk',
#     'country_emoji': '🇬🇧',
#     'country_name_ja': 'イギリス',
#     'description': '英国の高級スポーツカーメーカー、タタ傘下'
# }
```

#### Land Rover
```python
# 'Land Rover': {
#     'rss_url': 'https://media.landrover.com/rss',  # 要確認
#     'country': 'uk',
#     'country_emoji': '🇬🇧',
#     'country_name_ja': 'イギリス',
#     'description': '高級SUVの代表格、タタ・モーターズ傘下'
# }
```

### 🇸🇪 スウェーデン

#### Volvo
```python
# 'Volvo': {
#     'rss_url': 'https://www.media.volvocars.com/rss',  # 要確認
#     'country': 'sweden',
#     'country_emoji': '🇸🇪',
#     'country_name_ja': 'スウェーデン',
#     'description': '安全性の代名詞、吉利汽車傘下で電動化推進'
# }
```

---

## RSS URL確認方法

各メーカーのニュースルームで以下を確認：

1. **公式サイトのニュースルームにアクセス**
   - 例: https://newsroom.{manufacturer}.com
   - 例: https://media.{manufacturer}.com

2. **RSSフィードリンクを探す**
   - ページ下部の「RSS」「Feeds」アイコン
   - ニュースルームの「Subscribe」セクション
   - ブラウザのRSS自動検出機能

3. **フィードURLを取得**
   - XMLファイルのURLをコピー
   - 通常は `/rss` `/feed` `/rss.xml` などのパス

---

## 国コード一覧

| 国コード | 国旗絵文字 | 日本語国名 |
|---------|----------|----------|
| japan | 🇯🇵 | 日本 |
| usa | 🇺🇸 | アメリカ |
| germany | 🇩🇪 | ドイツ |
| south_korea | 🇰🇷 | 韓国 |
| italy | 🇮🇹 | イタリア |
| uk | 🇬🇧 | イギリス |
| sweden | 🇸🇪 | スウェーデン |
| france | 🇫🇷 | フランス |

---

## メーカー追加手順

1. **RSS URLを確認**
   - メーカー公式ニュースルームでRSSフィードを探す

2. **データを追加**
   - `news_collector.py` の `manufacturer_feeds` に以下の形式で追加:
   ```python
   'メーカー名': {
       'rss_url': 'RSSフィードURL',
       'country': '国コード',
       'country_emoji': '国旗絵文字',
       'country_name_ja': '日本語国名',
       'description': '詳細な特徴説明（20-30文字）'
   }
   ```

3. **接続テスト**
   ```bash
   source .venv/bin/activate
   python main.py --mode test
   ```

4. **RSS取得テスト**
   ```bash
   python main.py --mode new-cars --hours 168
   ```

---

## 統計情報

- **実装済みメーカー**: 15社
- **コメントアウト**: 10社
- **対応国**: 6カ国（日本、アメリカ、ドイツ、韓国、イタリア、イギリス）
- **将来追加予定**: スウェーデン（Volvo）、フランス（Renault等）

---

## 最終更新日
2026-02-01
