---
title: "Goの並列処理を理解する ── channelとselectの内部実装（第3回）"
source: "Zenn"
category: "it"
published: 2026-07-05T06:45:31
url: https://zenn.dev/wakame_atsushi/articles/1b9239f1b33faa
---

# Goの並列処理を理解する ── channelとselectの内部実装（第3回）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月05日 06:45
- **URL**: [https://zenn.dev/wakame_atsushi/articles/1b9239f1b33faa](https://zenn.dev/wakame_atsushi/articles/1b9239f1b33faa)

## 概要

はじめに
goroutine 同士が、互いに通信し、同期する役割を担うのが channel です。
ch &lt;- x   // 送信
v := &lt;-ch // 受信
この 1 行ずつの裏で、ランタイムは「受け取ってくれる相手はもういるか？ いなければ自分は眠って待ち、相手が来たら起こしてもらう」という段取りを踏んでいます。今回はその段取りを、channel の中身である hchan という構造体から読みます。
Go の並行処理には設計の出発点として一つの方針があります。Effective Go はこう書いています。

Do not communicate by sharin...

---

*この記事は自動収集システムによって保存されました。*
