# 🚀 本番運用ガイド

**最終更新**: 2026-03-01
**バージョン**: v3.0
**ステータス**: ✅ 本番運用開始

---

## 📊 システム概要

### 収集ソース（32ソース）

#### 💻 IT関連（19ソース）

**🇯🇵 日本語メディア（12）**
1. ITmedia News
2. ITmedia AI+
3. @IT
4. Publickey
5. GIZMODO Japan
6. TechCrunch Japan
7. Engadget日本版
8. CNET Japan
9. Zenn
10. Qiita (JavaScript)
11. Qiita (Python)
12. Qiita (React)

**🌍 グローバルメディア（2）**
13. The Verge
14. Hacker News

**☁️ クラウド・インフラ（3）**
15. AWS What's New
16. Microsoft DevBlogs
17. GitHub Blog

**🤖 AI企業公式（1）**
18. OpenAI Blog

**🔬 半導体・AIプラットフォーム（1）**
19. NVIDIA Newsroom

#### 🚗 車関連（13ソース）

**⚡ EVテックメディア（2）**
1. Electrek
2. InsideEVs

**🏭 メーカー公式RSS（11社）**
- 🇯🇵 日本: Toyota, Lexus, Honda, Nissan, Mazda
- 🇩🇪 ドイツ: Porsche, BMW
- 🇺🇸 アメリカ: GM, Ford, Tesla
- 🇰🇷 韓国: Hyundai, Kia
- 🇮🇹 イタリア: Lamborghini
- 🇬🇧 イギリス: Rolls-Royce

---

## 🎯 主要機能

| 機能 | 説明 | 頻度 |
|------|------|------|
| **日次配信** | IT/車ニュースを要約して配信 | 毎日8:00 JST |
| **重要度評価** | 星5段階で自動評価（デフォルト: ★3以上を配信） | 記事ごと |
| **英語翻訳** | 英語記事を日本語に自動翻訳 | 記事ごと |
| **新型車トラッキング** | 新型車発表を自動検出 | 週1回（月曜） |
| **Markdown保存** | GitHubに記事を自動保存 | 毎回 |

---

## ⚙️ 運用モード

### 1. 全ニュース配信（推奨）

```bash
# デフォルト（★3以上、24時間分）
python main.py --mode all

# 重要度を変更（★4以上のみ）
python main.py --mode all --importance 4

# 期間を変更（48時間分）
python main.py --mode all --hours 48
```

### 2. 新型車専用モード

```bash
# 新型車情報のみを検出・配信
python main.py --mode new-cars
```

### 3. 接続テスト

```bash
# Discord接続をテスト
python main.py --mode test
```

---

## 📅 GitHub Actions 自動実行

### 現在の設定

| ワークフロー | スケジュール | 実行内容 |
|------------|------------|---------|
| **daily-news.yml** | 毎日 8:00 JST | 全ニュース配信（★3以上） |
| **new-car-tracker.yml** | 毎週月曜 8:00 JST | 新型車情報検出 |

### 手動実行

1. GitHubリポジトリを開く
2. `Actions` タブをクリック
3. 実行したいワークフローを選択
4. `Run workflow` をクリック

---

## 💰 月間コスト（推定）

### リソース使用量

```
記事収集: 60-120件/日
├─ IT記事: 30-60件/日
│  ├─ 日本語: 15-30件
│  └─ 英語: 15-30件（→自動翻訳）
└─ 車記事: 30-60件/日
   ├─ EVメディア: 10-20件
   └─ メーカー公式: 20-40件
```

### API使用量（Poe API）

```
1日あたり:
├─ 翻訳: 30件 × 500トークン = 15,000トークン
├─ 重要度評価: 60件 × 500トークン = 30,000トークン
└─ 要約生成: 15件 × 2,000トークン = 30,000トークン
───────────────────────────────────────
合計: 75,000トークン/日

月間: 75,000 × 30 = 2,250,000トークン
```

### 料金

| モデル | 入力コスト | 出力コスト | 月額 | 円換算 |
|--------|-----------|-----------|------|--------|
| gpt-5-nano | $0.15/1M | $0.60/1M | **$0.45** | **約70円** |
| gemini-3-flash | $0.10/1M | $0.40/1M | **$0.32** | **約50円** |

**その他のコスト**: すべて無料
- Discord Webhook: 無料
- GitHub Actions: 無料枠内
- GitHub Storage: 無料

**合計月額**: 約50-70円 ☕️

---

## 📊 期待される成果

### 日次配信例

```
毎朝8:00にDiscordに通知:

【ITチャンネル】
📱 IT: 8件の重要記事
   ├─ ★★★★★ OpenAI GPT-5発表
   ├─ ★★★★☆ AWS新AI機能リリース
   ├─ ★★★☆☆ GitHubコパイロット更新
   └─ その他5件

【車チャンネル】
🚗 車: 5件の重要記事
   ├─ ★★★★★ テスラ新型Model発表
   ├─ ★★★★☆ トヨタEV新戦略
   └─ その他3件
```

### 情報のカバレッジ

```
【完全カバー】
✅ IT業界最新動向（AIからクラウドまで）
✅ EV・自動車業界（テックとメーカー両方）
✅ 開発者トレンド（Hacker News、Qiita、Zenn）

【部分カバー】
🟡 Anthropic（間接的にHacker Newsなどで）
🟡 Google DeepMind（間接的にThe Vergeなどで）

【未カバー】
⚪ 一部欧米メーカー（VW、Audi等）
⚪ 日本の自動車専門メディア
```

---

## 🔧 トラブルシューティング

### Discord配信が届かない

**確認事項**:
1. `.env` ファイルのWebhook URLが正しいか
2. `python main.py --mode test` で接続テスト
3. Discord側でWebhookが有効か

**解決策**:
```bash
# 環境変数を確認
cat .env | grep WEBHOOK

# テスト実行
python main.py --mode test
```

### 翻訳が動作しない

**確認事項**:
1. Poe API Keyが有効か
2. API残高があるか

**解決策**:
```bash
# 環境変数を確認
cat .env | grep POE_API_KEY

# ログを確認
python main.py --mode all --hours 6
```

### 記事が取得できない

**考えられる原因**:
- RSSフィードのURL変更
- ネットワーク接続の問題
- レート制限

**解決策**:
```bash
# テストスクリプトで個別確認
python test_strategic_feeds.py
python test_new_feeds.py
```

### GitHub Actionsが失敗する

**確認事項**:
1. Secretsが正しく設定されているか
2. Workflow permissionsが有効か

**解決策**:
1. Settings → Secrets → Actions で確認
2. Settings → Actions → General → Workflow permissions を "Read and write" に設定

---

## 📈 パフォーマンス指標

### 成功率の目安

```
通常時:
├─ 記事収集成功率: 95%以上
├─ 翻訳成功率: 98%以上
├─ 重要度評価成功率: 95%以上
└─ Discord配信成功率: 99%以上

異常時のアラート:
├─ 収集成功率 < 80%: RSSフィード確認
├─ 翻訳失敗 > 10%: Poe API確認
└─ Discord失敗 > 5%: Webhook確認
```

---

## 🔄 定期メンテナンス

### 週次（推奨）

- [ ] Discord通知を確認（記事の質と量）
- [ ] GitHub Actionsの実行ログを確認

### 月次（推奨）

- [ ] Poe API使用量と残高を確認
- [ ] RSSフィードの追加/削除を検討
- [ ] 重要度評価の精度を確認

### 四半期（任意）

- [ ] 新しい情報源の追加を検討
- [ ] システムの改善点を洗い出し
- [ ] コスト最適化の検討

---

## 🎯 今後の拡張案

### 短期的（必要に応じて）

- [ ] RSSHubセルフホスト（Docker）
- [ ] Anthropicなど重要サイトのスクレイピング
- [ ] Slackへの配信追加

### 中長期的（興味があれば）

- [ ] Webダッシュボード作成
- [ ] 音声ニュース生成
- [ ] トレンド分析機能
- [ ] ユーザー別カスタマイズ

---

## 📞 サポート情報

### ドキュメント

- `README.md` - 基本的な使い方
- `SPECIFICATION.md` - システム仕様
- `PRODUCTION_GUIDE.md` - 本ガイド（本番運用）

### テストスクリプト

- `test_new_feeds.py` - 新規RSSテスト
- `test_strategic_feeds.py` - 戦略的ソーステスト
- `test_rsshub_feeds.py` - RSSHubテスト

### フィードバック

問題や改善案があれば：
- GitHubでIssueを作成
- または直接コードを修正

---

## ✅ 本番運用チェックリスト

### 初回セットアップ

- [x] 依存パッケージをインストール（`pip install -r requirements.txt`）
- [x] `.env` ファイルを作成・設定
- [x] Discord Webhookを設定
- [x] Poe API Keyを設定
- [x] 接続テストを実行（`python main.py --mode test`）

### GitHub Actions設定

- [ ] GitHubリポジトリにSecretsを追加
  - [ ] `POE_API_KEY`
  - [ ] `IT_WEBHOOK_URL`
  - [ ] `CAR_WEBHOOK_URL`
  - [ ] `NEW_CAR_WEBHOOK_URL`
- [ ] Workflow permissionsを "Read and write" に設定
- [ ] 手動でワークフローを1回実行してテスト

### 本番運用開始

- [ ] 初回実行テスト（`python main.py --mode all --hours 6`）
- [ ] Discordに通知が届くことを確認
- [ ] GitHub Actionsの自動実行を有効化
- [ ] 翌朝8:00の配信を確認

---

## 🎉 運用開始おめでとうございます！

このシステムは**月額50-70円**で、毎日自動的に：

✅ **32の情報源**から最新ニュースを収集
✅ **英語記事を日本語に翻訳**
✅ **AI重要度評価**で重要記事を選別
✅ **Discord通知**で朝の情報収集を効率化
✅ **GitHub保存**でナレッジを蓄積

**IT×車の融合領域**を完全カバーする、超低コストの情報キュレーションシステムが稼働します！🚀

---

*最終更新: 2026-03-01*
