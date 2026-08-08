---
title: "1582年の改暦点を正しく扱える JavaScript 日付ライブラリを自作した話（ユリウス暦→グレゴリオ暦対応）"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-08T16:59:22
url: https://qiita.com/NAS6mixfoolv/items/7398e216adbb64632b1f
---

# 1582年の改暦点を正しく扱える JavaScript 日付ライブラリを自作した話（ユリウス暦→グレゴリオ暦対応）

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月08日 16:59
- **URL**: [https://qiita.com/NAS6mixfoolv/items/7398e216adbb64632b1f](https://qiita.com/NAS6mixfoolv/items/7398e216adbb64632b1f)

## 概要

はじめに
JavaScript の Date オブジェクトは、
1582 年のユリウス暦 → グレゴリオ暦の1582年の改暦（10日削除）を表現する用途には適していない。
例えば：

1582/10/4 の翌日が 1582/10/15 にならない
1582/10/5～14...

---

*この記事は自動収集システムによって保存されました。*
