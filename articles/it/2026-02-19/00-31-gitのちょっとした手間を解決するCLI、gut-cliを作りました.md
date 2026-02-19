---
title: "gitのちょっとした手間を解決するCLI、gut-cliを作りました"
source: "Zenn"
category: "it"
published: 2026-02-19T00:31:03
url: https://zenn.dev/steelydylan/articles/why-i-created-gut-cli
---

# gitのちょっとした手間を解決するCLI、gut-cliを作りました

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月19日 00:31
- **URL**: [https://zenn.dev/steelydylan/articles/why-i-created-gut-cli](https://zenn.dev/steelydylan/articles/why-i-created-gut-cli)

## 概要

はじめに
git commit -m "ここに何書こう..." ってなることありませんか？
これをgit commitだけにして、変更内容はAIに書いて欲しいなと思ってCLIツールを作りに着手しました。
Claude Codeでやれば？という話かもしれませんが、Claude Codeは汎用的なコーディングエージェントなのでファイル全体を読み込んでユーザーの許可を得てみたいな感じで
コミットメッセージを考えて欲しいだけなのに若干待たされるのが不便でした。
このCLI（gut-cli）だとこんな感じでサクサクです！

ブランチ名も同じです。GitHubのissueの内容を見て、featu...

---

*この記事は自動収集システムによって保存されました。*
