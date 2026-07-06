---
title: "ECMAScriptにおけるグレゴリオ暦: iso8601とgregory"
source: "Zenn"
category: "it"
published: 2026-07-05T07:57:21
url: https://zenn.dev/fabon/articles/c4b2efbb0c526b
---

# ECMAScriptにおけるグレゴリオ暦: iso8601とgregory

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月05日 07:57
- **URL**: [https://zenn.dev/fabon/articles/c4b2efbb0c526b](https://zenn.dev/fabon/articles/c4b2efbb0c526b)

## 概要

ECMAScriptにはTemporalやIntl.DateTimeFormatといった暦を扱うAPIが存在し、最もよく使われるグレゴリオ暦はもちろん、日本の元号、東アジアのいわゆる旧暦（太陰太陽暦）、ヒジュラ暦やユダヤ暦など多種多様な暦がサポートされています。そのうち一般的なグレゴリオ暦[1]を指すものとしてiso8601とgregoryが存在しますが、この両者の違いは何で、なぜ別のものとして存在しているのでしょうか?
短い解答は、gregoryは国際化の文脈で使われる現実のグレゴリオ暦である一方、iso8601はモデル化された「人工的」かつ文化中立的なグレゴリオ暦だということです。
...

---

*この記事は自動収集システムによって保存されました。*
