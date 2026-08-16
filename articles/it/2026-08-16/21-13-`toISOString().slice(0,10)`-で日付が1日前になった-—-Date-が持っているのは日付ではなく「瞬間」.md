---
title: "`toISOString().slice(0,10)` で日付が1日前になった — Date が持っているのは日付ではなく「瞬間」"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-16T21:13:35
url: https://qiita.com/daisuke-nagata/items/a3141b7aa7440cdfed51
---

# `toISOString().slice(0,10)` で日付が1日前になった — Date が持っているのは日付ではなく「瞬間」

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月16日 21:13
- **URL**: [https://qiita.com/daisuke-nagata/items/a3141b7aa7440cdfed51](https://qiita.com/daisuke-nagata/items/a3141b7aa7440cdfed51)

## 概要

日本時間の深夜0時に作った Date を、いつもの書き方で日付文字列にしたら、1日前の日付が出てきた。 

const d = new Date(2026, 7, 18, 0, 30); // JST 2026-08-18 00:30
d.toISOString().slic...

---

*この記事は自動収集システムによって保存されました。*
