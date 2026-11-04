---
title: "kintoneの参照先をたどる処理をJavaScriptでテストする｜循環参照・共通の参照先・深さ上限"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-04T02:08:37
url: https://qiita.com/kintaco/items/a4803563247dedb53196
---

# kintoneの参照先をたどる処理をJavaScriptでテストする｜循環参照・共通の参照先・深さ上限

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月04日 02:08
- **URL**: [https://qiita.com/kintaco/items/a4803563247dedb53196](https://qiita.com/kintaco/items/a4803563247dedb53196)

## 概要

アプリAからB、BからAへ参照しているとき、参照先をそのまま再帰的にたどると、同じアプリを繰り返し処理してしまいます。処理する予定に入れたIDをSetへ記録し、同じIDをもう一度キューへ入れないようにします。
今回はkintoneのアプリ間参照を題材に、メモリー上の小さな関...

---

*この記事は自動収集システムによって保存されました。*
