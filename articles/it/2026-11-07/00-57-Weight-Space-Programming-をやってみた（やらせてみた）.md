---
title: "Weight-Space Programming をやってみた（やらせてみた）"
source: "Zenn"
category: "it"
published: 2026-11-07T00:57:13
url: https://zenn.dev/nwn/articles/cf9fe78aa33861
---

# Weight-Space Programming をやってみた（やらせてみた）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月07日 00:57
- **URL**: [https://zenn.dev/nwn/articles/cf9fe78aa33861](https://zenn.dev/nwn/articles/cf9fe78aa33861)

## 概要

GPT-6 AstraにQwen3.5-0.8Bの重みを編集させることができたという論文が話題です。
https://x.com/rikiyatakehi/status/2117313742891327994
Xで反応を見ていると、AstraがQwenの重みを丸ごと読み込んで、その数値の意味を理解したように受け取られている場面がありました。実験でAstraがやったのは、コードを書いて対象モデルの重みや内部活性を調べ、挙動の仮説を立て、重みに変更を加えて結果を確かめることです。
今回の研究について、自分の理解はこうです。

「人間には不可能な能力が発見された」→ 違う
「重みを直接編集でき...

---

*この記事は自動収集システムによって保存されました。*
