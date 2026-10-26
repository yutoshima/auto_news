---
title: "Claude Codeにghを使わせても、GH_TOKENをコンテナの環境変数に置かないdevcontainer構成"
source: "Zenn"
category: "it"
published: 2026-10-25T06:03:07
url: https://zenn.dev/hii_chi/articles/claude-code-gh-token-wrapper
---

# Claude Codeにghを使わせても、GH_TOKENをコンテナの環境変数に置かないdevcontainer構成

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 06:03
- **URL**: [https://zenn.dev/hii_chi/articles/claude-code-gh-token-wrapper](https://zenn.dev/hii_chi/articles/claude-code-gh-token-wrapper)

## 概要

devcontainer で Claude Code が PR や Issue を作成できるように、GitHub CLI（gh）を利用させることにしました。そのためには、GitHub のトークンをコンテナに渡す必要があります。環境変数に入れれば手軽ですが、Claude Code がうっかり env を出力すると、トークンがそのまま表示されてしまいます。
この記事では、トークンを環境変数にも gh の設定ファイルにも置かずに gh を使える構成を、3 つのファイルに分けて紹介します。あわせて、この構成でも防げないことを、実際に試した結果とともに書きます。

 結論
本物の gh を PAT...

---

*この記事は自動収集システムによって保存されました。*
