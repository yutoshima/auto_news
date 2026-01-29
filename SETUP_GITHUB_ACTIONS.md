# GitHub Actions 自動実行セットアップガイド

## 📋 概要

2つのワークフローを設定しました：

1. **毎日のニュース配信** (`daily-news.yml`)
   - 毎朝8:00（JST）に実行
   - 過去24時間のニュースを要約して配信

2. **新型車情報トラッカー** (`new-car-tracker.yml`)
   - 3時間ごとに実行
   - 新型車・プロトタイプ情報を即座にキャッチ

## 🚀 セットアップ手順

### 1. GitHubリポジトリを作成

このプロジェクトをGitHubにプッシュします。

```bash
# Gitリポジトリを初期化
git init

# .gitignoreに.venvを追加（既に設定済み）
# すべてのファイルを追加
git add .

# 初回コミット
git commit -m "Initial commit: 車とITニュース自動配信システム"

# GitHubでリポジトリを作成後、リモートを追加
git remote add origin https://github.com/あなたのユーザー名/auto_news.git

# プッシュ
git branch -M main
git push -u origin main
```

### 2. GitHub Secretsを設定

GitHubリポジトリのSettings → Secrets and variables → Actions で以下を設定：

#### 必要なSecrets

1. **POE_API_KEY**
   - Name: `POE_API_KEY`
   - Secret: あなたのPoe APIキー

2. **DISCORD_WEBHOOK_URL**
   - Name: `DISCORD_WEBHOOK_URL`
   - Secret: あなたのDiscord Webhook URL

#### 設定手順

1. GitHubリポジトリページを開く
2. `Settings` タブをクリック
3. 左サイドバーの `Secrets and variables` → `Actions` をクリック
4. `New repository secret` をクリック
5. Name と Secret を入力して `Add secret`
6. 2つ目のSecretも同様に追加

### 3. ワークフローを有効化

GitHub Actionsは自動的に有効になりますが、念のため確認：

1. リポジトリの `Actions` タブをクリック
2. ワークフローが表示されていることを確認
3. 初回は手動で実行してテスト：
   - `毎日のニュース配信` をクリック
   - `Run workflow` ボタンをクリック
   - モードと時間を選択して実行

### 4. 実行スケジュール

#### 毎日のニュース配信
- **実行時刻**: 毎朝 8:00 JST (23:00 UTC)
- **モード**: 全ニュース要約 + 新型車検出
- **対象期間**: 過去24時間

#### 新型車トラッカー
- **実行頻度**: 3時間ごと
- **モード**: 新型車のみ
- **対象期間**: 過去6時間

## 🔧 カスタマイズ

### 実行時刻を変更したい場合

`.github/workflows/daily-news.yml` の以下の部分を編集：

```yaml
schedule:
  - cron: '0 23 * * *'  # ← ここを変更
```

**Cron式の例：**
- `0 0 * * *` - 毎日 9:00 JST (0:00 UTC)
- `0 22 * * *` - 毎日 7:00 JST (22:00 UTC前日)
- `0 12 * * *` - 毎日 21:00 JST (12:00 UTC)

参考: [Crontab Guru](https://crontab.guru/)

### 新型車チェックの頻度を変更

`.github/workflows/new-car-tracker.yml` の以下の部分を編集：

```yaml
schedule:
  - cron: '0 */3 * * *'  # ← */3 を他の数字に変更
```

- `*/1` - 1時間ごと（最頻繁）
- `*/6` - 6時間ごと
- `*/12` - 12時間ごと

## 📊 実行結果の確認

1. GitHubリポジトリの `Actions` タブを開く
2. 実行履歴が表示される
3. 各実行をクリックすると詳細ログが見られる
4. エラーが発生した場合もここで確認可能

## ⚠️ 注意事項

### GitHub Actionsの無料枠

- **Public リポジトリ**: 完全無料
- **Private リポジトリ**: 月2,000分まで無料

このプロジェクトの1回の実行時間は約1-2分なので、月間コスト:
- 1日1回: 30分/月 → 無料枠内
- 1日8回（3時間ごと）: 240分/月 → 無料枠内
- **合計**: 270分/月程度 → 無料枠内で十分収まる

### タイムゾーンについて

GitHub ActionsのCronはUTC（協定世界時）で動作します。
- JST (日本時間) = UTC + 9時間
- 8:00 JST = 23:00 UTC（前日）

## 🎯 トラブルシューティング

### ワークフローが実行されない

1. Secretsが正しく設定されているか確認
2. `.github/workflows/` ディレクトリが正しくプッシュされているか確認
3. GitHubのActions タブでエラーメッセージを確認

### Discordに通知が来ない

1. Webhook URLが正しいか確認
2. Webhookが削除されていないか確認
3. GitHub Actionsのログでエラーを確認

### LLMエラーが出る

1. Poe API Keyが正しいか確認
2. Poe APIの残高を確認
3. モデル名が正しいか確認（`gemini-3-flash`）

## 🔄 更新方法

コードを修正した場合：

```bash
git add .
git commit -m "更新内容の説明"
git push
```

次回の自動実行から新しいコードが適用されます。

## 📱 手動実行

自動実行を待たずに今すぐ実行したい場合：

1. GitHubリポジトリの `Actions` タブを開く
2. 実行したいワークフローを選択
3. `Run workflow` ボタンをクリック
4. パラメータを選択して実行

これで完了です！🎉
