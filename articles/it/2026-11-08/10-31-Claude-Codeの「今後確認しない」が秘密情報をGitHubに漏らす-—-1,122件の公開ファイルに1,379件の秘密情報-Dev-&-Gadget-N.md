---
title: "Claude Codeの「今後確認しない」が秘密情報をGitHubに漏らす — 1,122件の公開ファイルに1,379件の秘密情報 - Dev & Gadget Note"
source: "はてブ テクノロジー"
category: "it"
published: 2026-11-08T10:31:52
url: https://dev.ponkotsu.dev/entry/claude-code-settings-local-secrets
---

# Claude Codeの「今後確認しない」が秘密情報をGitHubに漏らす — 1,122件の公開ファイルに1,379件の秘密情報 - Dev & Gadget Note

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年11月08日 10:31
- **URL**: [https://dev.ponkotsu.dev/entry/claude-code-settings-local-secrets](https://dev.ponkotsu.dev/entry/claude-code-settings-local-secrets)

## 概要

Claude Codeで「Yes, and don't ask again（今後確認しない）」を選ぶと、承認したコマンドがそのままプロジェクト内の.claude/settings.local.jsonに保存されます。コマンドにパスワードやAPIキーが含まれていると、平文のまま残ります。セキュリティ企業Apiiroの調査（11月7日公表）では、公開GitHubリポジトリにある...

---

*この記事は自動収集システムによって保存されました。*
