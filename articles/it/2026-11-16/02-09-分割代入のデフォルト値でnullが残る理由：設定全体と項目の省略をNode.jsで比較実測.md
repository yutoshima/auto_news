---
title: "分割代入のデフォルト値でnullが残る理由：設定全体と項目の省略をNode.jsで比較実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-16T02:09:56
url: https://qiita.com/ennagara128/items/8f1da0196ccf5ce2685c
---

# 分割代入のデフォルト値でnullが残る理由：設定全体と項目の省略をNode.jsで比較実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月16日 02:09
- **URL**: [https://qiita.com/ennagara128/items/8f1da0196ccf5ce2685c](https://qiita.com/ennagara128/items/8f1da0196ccf5ce2685c)

## 概要

APIの設定に null が入っていたとき、const { limit = 10 } = options なら10件になると思っていませんか。分割代入のデフォルト値が使われるのは、取り出した値が undefined のときだけです。null はそのまま残ります。

実行環境...

---

*この記事は自動収集システムによって保存されました。*
