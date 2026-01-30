# Discord Bot セットアップガイド

## 1. Discord Botの作成

### 1.1 Discord Developer Portalにアクセス
https://discord.com/developers/applications

### 1.2 新しいアプリケーションを作成
1. 「New Application」をクリック
2. Bot名を入力（例: 車とITニュースBot）
3. 「Create」をクリック

### 1.3 Botを追加
1. 左メニューから「Bot」を選択
2. 「Add Bot」をクリック
3. 「Yes, do it!」で確認

### 1.4 Botトークンを取得
1. 「TOKEN」セクションの「Reset Token」をクリック
2. 表示されたトークンをコピー
3. `.env`ファイルの`DISCORD_BOT_TOKEN`に設定

```bash
DISCORD_BOT_TOKEN=your_token_here
```

### 1.5 必要な権限を有効化
「Privileged Gateway Intents」セクションで以下を有効化：
- ✅ MESSAGE CONTENT INTENT

## 2. Botをサーバーに招待

### 2.1 OAuth2 URLを生成
1. 左メニューから「OAuth2」→「URL Generator」を選択
2. **SCOPES**で`bot`を選択
3. **BOT PERMISSIONS**で以下を選択：
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Read Messages/View Channels
4. 生成されたURLをコピーしてブラウザで開く
5. Botを追加したいサーバーを選択

## 3. Botの起動

### 3.1 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

### 3.2 Botを起動
```bash
# 起動スクリプトを使用
./start_bot.sh

# または直接実行
python discord_bot.py
```

### 3.3 動作確認
Discord上で：
```
@ボット名 こんにちは
```

## 4. 使い方

### 質問する
Botをメンションして質問：
```
@ボット名 今日のITニュースは？
@ボット名 最近の新型車情報を教えて
@ボット名 AIに関する記事はある？
```

### コマンド
```
!help - ヘルプを表示
!status - Bot状態確認
```

## 5. Raspberry Piで常時起動（オプション）

### 5.1 systemdサービスを作成
`/etc/systemd/system/discord-news-bot.service`
```ini
[Unit]
Description=Discord News Bot
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/auto_news
ExecStart=/home/pi/auto_news/.venv/bin/python /home/pi/auto_news/discord_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 5.2 サービスを有効化
```bash
sudo systemctl daemon-reload
sudo systemctl enable discord-news-bot
sudo systemctl start discord-news-bot

# 状態確認
sudo systemctl status discord-news-bot
```

## トラブルシューティング

### Botが応答しない
1. `MESSAGE CONTENT INTENT`が有効化されているか確認
2. Botトークンが正しく設定されているか確認
3. Botがサーバーにいるか確認

### エラーログの確認
```bash
# サービスのログを確認
sudo journalctl -u discord-news-bot -f
```

## 注意事項

- Botトークンは絶対に公開しないでください
- `.env`ファイルは`.gitignore`に含めてください
- Botは24時間起動しておく必要があります（定期配信は別途GitHub Actionsで実行）
