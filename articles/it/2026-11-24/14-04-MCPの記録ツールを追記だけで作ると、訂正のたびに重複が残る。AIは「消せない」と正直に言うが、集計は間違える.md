---
title: "MCPの記録ツールを追記だけで作ると、訂正のたびに重複が残る。AIは「消せない」と正直に言うが、集計は間違える"
source: "Zenn"
category: "it"
published: 2026-11-24T14:04:27
url: https://zenn.dev/kentaro_tak/articles/mcp-logger-append-only-corrections
---

# MCPの記録ツールを追記だけで作ると、訂正のたびに重複が残る。AIは「消せない」と正直に言うが、集計は間違える

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月24日 14:04
- **URL**: [https://zenn.dev/kentaro_tak/articles/mcp-logger-append-only-corrections](https://zenn.dev/kentaro_tak/articles/mcp-logger-append-only-corrections)

## 概要

家の記録を、Claude Codeに書かせている。その日にやったことの時間、休肝日、一言日記、外食、子どもの記録など、Googleスプレッドシートに書き込むMCPのツールが7つある（家の用事をClaude Codeに任せている話は、個人ブログにまとめている）。
作ってから気づいたのは、7つのうち6つが「追記」と「読む」しか持っていなかったことだ。中身はシートAPIの values().append で、同じ日付でもう一度呼ぶと、新しい行が足される。例外は時間の記録だけで、こちらは同じ日付で呼ぶと、その日の行を全部置き換える。
困ったのは、訂正が来た日だった。休肝日を「◯（飲まなかった）」...

---

*この記事は自動収集システムによって保存されました。*
