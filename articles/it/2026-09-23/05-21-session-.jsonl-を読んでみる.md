---
title: "<session>.jsonl を読んでみる"
source: "Zenn"
category: "it"
published: 2026-09-23T05:21:00
url: https://zenn.dev/yando/articles/fdbe38474378d2
---

# <session>.jsonl を読んでみる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月23日 05:21
- **URL**: [https://zenn.dev/yando/articles/fdbe38474378d2](https://zenn.dev/yando/articles/fdbe38474378d2)

## 概要

はじめに
Claude Codeのセッションは、~/.claude/projects/&lt;project&gt;/&lt;session&gt;.jsonl に1行1イベントの形式で全て記録されています。
ただ、コスト・会話の流れ・コンテキストの中身がそれぞれどのフィールドに現れるか、そしてjqでどう叩けば見えるかは、実際に手を動かさないと分かりません。
今回はclaude -p(ヘッドレスモード)でいくつかパターンの違う指示を新規に実行し、生成されたjsonlをその場でjqで見比べながら、「コスト」「会話フロー」「コンテキスト」の3観点で可視化する方法を確認します。



用語...

---

*この記事は自動収集システムによって保存されました。*
