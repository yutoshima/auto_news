---
title: "filter(Boolean)で0やfalseが消える理由：欠損値だけを除く条件をNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-13T00:58:05
url: https://qiita.com/ennagara128/items/867a7e870f8ffa0be9a0
---

# filter(Boolean)で0やfalseが消える理由：欠損値だけを除く条件をNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月13日 00:58
- **URL**: [https://qiita.com/ennagara128/items/867a7e870f8ffa0be9a0](https://qiita.com/ennagara128/items/867a7e870f8ffa0be9a0)

## 概要

filter(Boolean) は null と undefined だけを消す書き方ではありません。数値の 0、空文字列、false、NaN も消えます。欠損値だけを除きたい一覧に使うと、有効な入力まで落としてしまいます。

Q. 0円の商品が一覧から消えるのはなぜ？
次...

---

*この記事は自動収集システムによって保存されました。*
