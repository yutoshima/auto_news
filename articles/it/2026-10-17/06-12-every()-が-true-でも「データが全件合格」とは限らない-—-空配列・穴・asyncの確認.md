---
title: "every() が true でも「データが全件合格」とは限らない — 空配列・穴・asyncの確認"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-17T06:12:07
url: https://qiita.com/ennagara128/items/c732b0baf8f7f1770ff9
---

# every() が true でも「データが全件合格」とは限らない — 空配列・穴・asyncの確認

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 06:12
- **URL**: [https://qiita.com/ennagara128/items/c732b0baf8f7f1770ff9](https://qiita.com/ennagara128/items/c732b0baf8f7f1770ff9)

## 概要

items.every(check) が true なら送信可能、とするコード。データがそもそも届いていなくても、その判定を通ることがあります。every は「1件以上あること」まで保証しません。
今回は、Node.js v24.14.1で返り値とコールバックの実行回数を確...

---

*この記事は自動収集システムによって保存されました。*
