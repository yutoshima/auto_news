---
title: "Promise.allで失敗した後も処理が続く：部分成功と中止を分けて設計する"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-09T00:44:32
url: https://qiita.com/CodeNest_media/items/eb204d3e8cc30c33ca54
---

# Promise.allで失敗した後も処理が続く：部分成功と中止を分けて設計する

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月09日 00:44
- **URL**: [https://qiita.com/CodeNest_media/items/eb204d3e8cc30c33ca54](https://qiita.com/CodeNest_media/items/eb204d3e8cc30c33ca54)

## 概要

三つのAPIをまとめて読み込み、一つが失敗したのでエラー画面にした。ところがサーバーログを見ると、残りの処理はまだ動いている。もう一度読み込むと、前の処理と次の処理が重なってしまう。
Promise.allの失敗は、すでに始まった仕事を全部取り消す合図ではありません。集めて...

---

*この記事は自動収集システムによって保存されました。*
