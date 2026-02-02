# 並行実装計画：スクレイピング + RSS再調査

## 実装日
2026-02-01

## 目標
1. スクレイピング機能を5社（Mercedes-Benz, Audi, Volkswagen, Jaguar, Land Rover）に実装
2. RSS URL再調査を5社（Nissan, BMW, Chevrolet, Cadillac, Volvo）に実施

---

## Track 1: スクレイピング実装（5社）

### 対象メーカー（robots.txt許可済み）
- ✅ Mercedes-Benz
- ✅ Audi
- ✅ Volkswagen
- ✅ Jaguar
- ✅ Land Rover

### 実装ステップ

#### Step 1: news_scraper.py の実装
- [ ] ScrapingCheckerをベースにNewScraperクラスを作成
- [ ] HTML構造の詳細分析機能を追加
- [ ] セレクタパターンの自動検出
- [ ] エラーハンドリングとフォールバック

#### Step 2: 各メーカーのHTML構造分析
- [  ] Mercedes-Benz: セレクタパターン特定
- [ ] Audi: セレクタパターン特定
- [ ] Volkswagen: セレクタパターン特定
- [ ] Jaguar: セレクタパターン特定
- [ ] Land Rover: セレクタパターン特定

#### Step 3: news_collector.pyへの統合
- [ ] ScraperインスタンスをNewsCollectorに追加
- [ ] `--use-scraping` オプションの実装
- [ ] メーカー情報（国、特徴）をスクレイピングデータに追加

#### Step 4: テストと検証
- [ ] 各メーカーでの取得テスト
- [ ] データ品質の確認
- [ ] パフォーマンス測定

---

## Track 2: RSS URL再調査（5社）

### 対象メーカー
- 🔍 Nissan
- 🔍 BMW
- 🔍 Chevrolet
- 🔍 Cadillac
- 🔍 Volvo

### 調査ステップ

#### Step 1: 公式ニュースルームの確認
各メーカーの公式サイトで以下を確認：
- [ ] Nissan: https://global.nissannews.com/
- [ ] BMW: https://www.press.bmwgroup.com/
- [ ] Chevrolet: https://media.chevrolet.com/
- [ ] Cadillac: https://media.cadillac.com/
- [ ] Volvo: https://www.media.volvocars.com/

#### Step 2: RSS URLの探索方法
1. **ページソースで検索**
   - `Ctrl+U` でページソースを表示
   - `Ctrl+F` で "rss", "feed", "atom" を検索

2. **RSSアイコンを探す**
   - ページ内のRSSアイコンをクリック
   - ブラウザのアドレスバーにRSSマークがあるか確認

3. **よくあるRSS URLパターンを試す**
   ```
   /rss
   /feed
   /rss.xml
   /feed.xml
   /news/rss
   /press-releases/rss
   ```

4. **開発者ツールで確認**
   - F12でDevToolsを開く
   - `<link rel="alternate" type="application/rss+xml"` を検索

#### Step 3: 発見したRSS URLを記録
見つかったRSS URLを以下の形式で記録：

```python
{
    'メーカー名': {
        'rss_url': '発見したURL',
        'country': '国コード',
        'country_emoji': '国旗絵文字',
        'country_name_ja': '日本語国名',
        'description': '特徴説明'
    }
}
```

---

## 優先順位

### Phase 1: 調査優先（1日目）
1. **RSS再調査を優先**
   - RSSが見つかればスクレイピング不要
   - 5社の調査を完了

2. **スクレイピング準備**
   - news_scraper.pyの基礎実装
   - HTML分析ツールの作成

### Phase 2: 実装（2日目）
1. **RSS発見済みメーカー**
   - news_collector.pyに追加
   - テスト実行

2. **RSS未発見メーカー**
   - スクレイピング実装
   - セレクタパターン設定

### Phase 3: テストと統合（3日目）
1. **全メーカーのテスト**
2. **エラーハンドリング強化**
3. **ドキュメント更新**

---

## 成功基準

### RSS再調査
- ✅ 5社中3社以上でRSS URLを発見
- ✅ 発見したRSS URLが正常に動作
- ✅ news_collector.pyに統合完了

### スクレイピング実装
- ✅ 5社中3社以上で記事取得成功
- ✅ robots.txt遵守
- ✅ 適切なレート制限（2-3秒間隔）
- ✅ エラーハンドリング実装

---

## リスク管理

### リスク1: RSS URLが見つからない
**対策:** スクレイピングに切り替え

### リスク2: スクレイピングがサイト変更で失敗
**対策:**
- 詳細なエラーログ
- フォールバック機能
- 定期的なメンテナンス

### リスク3: 実装時間がかかりすぎる
**対策:**
- 優先順位を明確化
- 最小限の機能から実装
- 段階的リリース

---

## 次のステップ

### 今すぐ開始
1. **RSS再調査ツール作成** - 5社のRSS URLを自動探索
2. **HTML分析ツール作成** - スクレイピング対象のHTML構造を分析

### 明日以降
1. RSS発見済みメーカーを追加
2. スクレイピング実装
3. テストと検証

---

## 実装担当
Claude Code (claude-sonnet-4-5-20250929)

## 実装開始日
2026-02-01
