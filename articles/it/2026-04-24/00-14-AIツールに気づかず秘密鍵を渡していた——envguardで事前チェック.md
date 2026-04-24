---
title: "AIツールに気づかず秘密鍵を渡していた——envguardで事前チェック"
source: "Zenn"
category: "it"
published: 2026-04-24T00:14:05
url: https://zenn.dev/winky/articles/envguard-ai-env-secret
---

# AIツールに気づかず秘密鍵を渡していた——envguardで事前チェック

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月24日 00:14
- **URL**: [https://zenn.dev/winky/articles/envguard-ai-env-secret](https://zenn.dev/winky/articles/envguard-ai-env-secret)

## 概要

はじめに
Claude Code や Cursor を日常的に使っている方に、一度確認してほしいことがあります。
AIツールを起動する前に、こんな設定が ~/.zshrc に残っていませんか。
export AWS_SECRET_ACCESS_KEY="AKIA..."
export GITHUB_TOKEN="ghp_..."
export OPENAI_API_KEY="sk-..."
もしそうなら、AIツールを起動するたびにこれらの値も一緒に渡しています。意図せず、毎回。
この記事では、なぜそうなるのか・どこに秘密情報が潜んでいるかを説明し、一括でチェックできるツール envg...

---

*この記事は自動収集システムによって保存されました。*
