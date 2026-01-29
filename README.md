# 🚗💻 車とITニュース自動配信システム

毎朝、車とITの最新ニュースをLLMで要約してDiscordに自動配信するサービスです。
世界中の新型車情報も見逃しません！

## 特徴

- 📰 日本の主要メディアからRSSで自動収集
- 🤖 Poe API（Gemini等）を使用した高品質な要約
- 🚨 新型車・プロトタイプの自動検出
- 💬 Discordへのリッチな通知
- 💰 低コスト運用（月額数十円〜）

## セットアップ

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env.example` をコピーして `.env` ファイルを作成：

```bash
cp .env.example .env
```

`.env` ファイルを編集して以下の値を設定：

```bash
# Poe API Key（https://poe.com/api_key から取得）
POE_API_KEY=your_poe_api_key_here

# Discord Webhook URL（後述の手順で取得）
DISCORD_WEBHOOK_URL=your_discord_webhook_url_here

# 使用するモデル（gemini-3-flash がおすすめ）
POE_MODEL=gemini-3-flash
```

### 3. Discord Webhook URLの取得方法

1. Discordで通知を受け取りたいサーバーを開く
2. 歯車アイコン（サーバー設定）をクリック
3. 「連携サービス」→「ウェブフック」を選択
4. 「新しいウェブフック」をクリック
5. 名前を設定（例: "ニュースBot"）
6. 「ウェブフックURLをコピー」をクリック
7. `.env` ファイルに貼り付け

### 4. Poe API Keyの取得方法

1. https://poe.com にアクセスしてログイン
2. https://poe.com/api_key にアクセス
3. API Keyを作成・コピー
4. `.env` ファイルに貼り付け

## 使い方

### 接続テスト

まず、Discord接続が正しく設定されているか確認：

```bash
python main.py --mode test
```

成功すると Discord にテストメッセージが届きます。

### 全ニュースの配信

過去24時間のニュースを要約して配信：

```bash
python main.py --mode all
```

過去48時間のニュースを取得したい場合：

```bash
python main.py --mode all --hours 48
```

### 新型車情報のみ配信

新型車・プロトタイプの情報のみを検出して配信：

```bash
python main.py --mode new-cars
```

## 自動実行の設定

### macOS/Linux の場合（cron）

毎朝8時に実行する例：

```bash
crontab -e
```

以下を追加：

```
0 8 * * * cd /Users/yuto/Documents/auto_news && /usr/local/bin/python3 main.py --mode all
```

### GitHub Actions で実行（推奨）

後日、GitHub Actions の設定ファイルを追加予定。
GitHub の無料枠で自動実行できます。

## プロジェクト構成

```
auto_news/
├── main.py                 # メインスクリプト
├── news_collector.py       # ニュース収集モジュール
├── news_analyzer.py        # LLM分析モジュール
├── discord_notifier.py     # Discord通知モジュール
├── requirements.txt        # 依存パッケージ
├── .env                    # 環境変数（要作成）
├── .env.example           # 環境変数のサンプル
└── README.md              # このファイル
```

## 利用可能なモデル

Poe APIでは以下のモデルが使用できます：

- `gemini-3-flash` - おすすめ（高速・低コスト）
- `gpt-4o-mini` - OpenAI（高品質）
- `claude-3.5-sonnet` - Anthropic（高精度）

## コスト目安

**gemini-3-flash を使用した場合：**
- 1日50記事処理: 約0.5円
- 月間コスト: 約15円

**gpt-4o-mini を使用した場合：**
- 1日50記事処理: 約1円
- 月間コスト: 約30円

## トラブルシューティング

### Discord に送信されない

1. `.env` ファイルの `DISCORD_WEBHOOK_URL` が正しいか確認
2. `python main.py --mode test` で接続テストを実行

### LLMエラーが出る

1. `.env` ファイルの `POE_API_KEY` が正しいか確認
2. Poe API の残高を確認
3. 別のモデルに変更してみる

### RSS取得エラー

一部のRSSフィードが取得できなくても、他のソースから取得を継続します。
ネットワーク接続を確認してください。

## 今後の拡張予定

- [ ] GitHub Actions による自動実行
- [ ] 画像認識によるスパイショット判定
- [ ] YouTube動画の要約機能
- [ ] Notion/Googleスプレッドシート連携
- [ ] トレンド分析と週次レポート
- [ ] 音声ニュース生成

## ライセンス

MIT License

## 作者

個人用プロジェクト
