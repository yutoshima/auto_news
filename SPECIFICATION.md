# 車とITニュース自動配信システム - 仕様書

## システム概要

車とIT業界のニュースを自動収集・分析し、重要度に基づいてDiscordに配信するシステム。

**バージョン**: 2.0
**最終更新**: 2026-01-31
**使用モデル**: gpt-5-nano (Poe API経由)

---

## 主要機能

### 1. ニュース自動収集
- **収集元**: RSS/Atomフィード（30以上の情報源）
- **カテゴリ**: IT / 車
- **実行頻度**: 毎日1回（8:00 JST）
- **保存形式**: Markdown（GitHubリポジトリに自動保存）

### 2. AI による重要度評価
- **評価方式**: 星5段階 (★☆☆☆☆ ～ ★★★★★)
- **配信基準**: ★3以上のみ詳細配信
- **★1-2**: 簡易リスト形式で表示
- **評価項目**: 技術革新性、業界影響度、一般関心度

### 3. マルチチャンネル配信
- **ITチャンネル**: IT関連ニュース専用
- **車チャンネル**: 車関連ニュース専用
- **新車チャンネル**: 新型車情報専用

### 4. 新型車トラッキング
- **実行頻度**: 週1回（月曜 8:00 JST）
- **検出対象**: 新型車、フルモデルチェンジ、コンセプトカー等
- **信頼度**: 70%以上のみ配信

---

## システム構成

```
auto_news/
├── main.py                    # メイン実行スクリプト
├── news_collector.py          # ニュース収集モジュール
├── news_analyzer.py           # AI分析・評価モジュール
├── discord_notifier.py        # Discord配信モジュール
├── article_storage.py         # 記事保存モジュール
├── requirements.txt           # 依存パッケージ
├── .env                       # 環境変数（機密情報）
├── .github/workflows/
│   ├── daily-news.yml        # 日次配信ワークフロー
│   └── new-car-tracker.yml   # 新型車トラッカー
└── articles/                  # 記事保存ディレクトリ
    ├── it/
    │   └── YYYY-MM-DD/
    │       └── HH-MM-記事タイトル.md
    └── car/
        └── YYYY-MM-DD/
            └── HH-MM-記事タイトル.md
```

---

## 情報源リスト

### IT関連 (12サイト)
- ITmedia News
- ITmedia AI+
- @IT
- Publickey
- GIZMODO Japan
- TechCrunch Japan
- Engadget日本版
- CNET Japan
- Zenn
- Qiita (JavaScript)
- Qiita (Python)
- Qiita (React)

### 車関連 (3サイト + メーカー公式)
- Car Watch
- Response
- Autoblog Japan
- Toyota Global
- Honda
- Tesla

---

## 環境変数

```bash
# Poe API設定
POE_API_KEY=<あなたのPoe APIキー>
POE_MODEL=gpt-5-nano

# Discord Webhook設定
IT_WEBHOOK_URL=<ITチャンネルのWebhook URL>
CAR_WEBHOOK_URL=<車チャンネルのWebhook URL>
NEW_CAR_WEBHOOK_URL=<新車チャンネルのWebhook URL>
```

---

## 使用方法

### ローカル実行

```bash
# 依存パッケージのインストール
pip install -r requirements.txt

# 全ニュース配信（デフォルト: ★3以上）
python main.py --mode all

# 重要度★4以上のみ配信
python main.py --mode all --importance 4

# 新型車情報のみ
python main.py --mode new-cars

# 接続テスト
python main.py --mode test

# カスタム期間指定（48時間前まで）
python main.py --mode all --hours 48
```

### GitHub Actions（自動実行）

**日次配信**:
- スケジュール: 毎日 8:00 JST (23:00 UTC前日)
- ワークフロー: `.github/workflows/daily-news.yml`

**新型車トラッカー**:
- スケジュール: 毎週月曜 8:00 JST (日曜 23:00 UTC)
- ワークフロー: `.github/workflows/new-car-tracker.yml`

**手動実行**:
- GitHubリポジトリ → Actions → ワークフロー選択 → "Run workflow"

---

## 出力フォーマット

### Discord配信形式

**ヘッダー**:
```
## 💻 今日のITニュース (2026年1月31日)
```

**記事（★3以上）**:
```
1. [AI] GoogleがGemini 3.0を発表
• 前世代比10倍の性能向上
• 推論速度が大幅に改善
• 業界標準を塗り替える可能性
```

**その他の記事（★1-2）**:
```
### その他の記事（★1-2）:
- ★★☆☆☆ Chrome拡張機能のアップデート情報 (ITmedia)
- ★☆☆☆☆ 個人ブログの技術記事 (Qiita)
```

**記事リンク**:
```
## 📎 記事リンク

1. [GoogleがGemini 3.0を発表...](https://example.com/1) - *TechCrunch*
2. [Meta、新AIモデル発表...](https://example.com/2) - *Engadget*
```

### Markdown保存形式

```markdown
---
title: "記事タイトル"
source: "情報源名"
category: "it"
published: 2026-01-31T10:00:00
url: https://example.com/article
---

# 記事タイトル

## メタデータ

- **情報源**: TechCrunch Japan
- **カテゴリ**: it
- **公開日時**: 2026年01月31日 10:00
- **URL**: [https://example.com/article](https://example.com/article)

## 概要

記事の概要が入ります...

---

*この記事は自動収集システムによって保存されました。*
```

---

## 重要度評価基準

| 星 | 評価 | 説明 | 配信方法 |
|----|------|------|----------|
| ★★★★★ | 5 | 業界を変える革新的発表 | 詳細配信 |
| ★★★★☆ | 4 | 非常に重要なニュース | 詳細配信 |
| ★★★☆☆ | 3 | 注目すべきニュース | 詳細配信 |
| ★★☆☆☆ | 2 | 一般的なニュース | リスト表示 |
| ★☆☆☆☆ | 1 | あまり重要でない | リスト表示 |

---

## 新型車判定基準

### ✅ 対象
- 完全新型モデルの発表
- フルモデルチェンジ
- マイナーチェンジ・フェイスリフト
- コンセプトカーの公開
- プロトタイプ・テスト車両
- 特別仕様車・限定モデル

### ❌ 除外
- 単純な販売開始・価格発表
- 決算・業績発表
- 人事異動
- リコール情報
- レース結果

---

## API使用量（概算）

### 月間トークン使用量
```
1日の処理:
- 30記事 × 重要度評価(500トークン) = 15,000トークン
- 10記事 × 要約生成(2,000トークン) = 20,000トークン
- 合計: 35,000トークン/日

月間合計: 35,000 × 30 = 1,050,000トークン
```

### 推定コスト（gpt-5-nano）
```
入力: 800,000トークン × $0.15/1M = $0.12
出力: 250,000トークン × $0.60/1M = $0.15
合計: 約$0.27/月 (約40円/月)
```

---

## GitHub Actions設定

### 必須設定

**リポジトリ Secrets**:
- `POE_API_KEY`
- `IT_WEBHOOK_URL`
- `CAR_WEBHOOK_URL`
- `NEW_CAR_WEBHOOK_URL`

**Workflow permissions**:
- Settings → Actions → General → Workflow permissions
- **"Read and write permissions"** を選択 ✅

---

## トラブルシューティング

### GitHub Actions のpushが失敗する
**エラー**: `Permission denied to github-actions[bot]`

**解決方法**:
1. リポジトリ設定で "Workflow permissions" を確認
2. "Read and write permissions" を選択
3. 保存して次回実行を待つ

### Discord配信が失敗する
- Webhook URLが正しいか確認
- URLの有効期限が切れていないか確認
- `!status` コマンドで接続テスト

### 記事が収集されない
- RSSフィードのURL変更を確認
- `news_collector.py` のフィード一覧を確認
- ネットワーク接続を確認

### 重要度評価が0になる
- Poe APIキーの有効性を確認
- API制限に達していないか確認
- モデル名が正しいか確認 (`POE_MODEL=gpt-5-nano`)

---

## 今後の拡張案

### 検討中の機能
- [ ] Slackへの配信対応
- [ ] Eメール配信
- [ ] Webダッシュボード
- [ ] ローカルLLM対応（Raspberry Pi）
- [ ] 多言語対応
- [ ] カスタムフィルター設定
- [ ] トレンド分析機能

### 将来的な改善
- [ ] 重要度評価精度の向上
- [ ] 記事の重複検出
- [ ] 画像の自動取得・保存
- [ ] RSS以外の情報源対応
- [ ] ユーザー別カスタマイズ

---

## ライセンス・謝辞

**開発**: Yuto Shima
**AI支援**: Claude Sonnet 4.5 (Anthropic)
**使用API**: Poe API
**配信**: Discord Webhook

---

## 変更履歴

### v2.0 (2026-01-31)
- 星5段階評価システムに変更
- マルチチャンネル配信対応
- IT情報源を12サイトに拡充
- 記事のMarkdown保存機能追加
- 重要度基準による自動フィルタリング

### v1.0 (2026-01-29)
- 初版リリース
- 基本的なニュース収集・配信機能
- 新型車トラッキング機能
