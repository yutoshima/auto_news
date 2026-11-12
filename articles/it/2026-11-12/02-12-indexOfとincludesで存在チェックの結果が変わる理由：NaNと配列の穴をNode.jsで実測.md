---
title: "indexOfとincludesで存在チェックの結果が変わる理由：NaNと配列の穴をNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-12T02:12:34
url: https://qiita.com/ennagara128/items/126397b4116a2377c7ff
---

# indexOfとincludesで存在チェックの結果が変わる理由：NaNと配列の穴をNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月12日 02:12
- **URL**: [https://qiita.com/ennagara128/items/126397b4116a2377c7ff](https://qiita.com/ennagara128/items/126397b4116a2377c7ff)

## 概要

indexOf(NaN) は -1 でも includes(NaN) は true。「含まれるか」を調べるコードでも、比較の規則は同じとは限りません。
AIが書いた存在チェックは、戻り値と比較方法を分けて確認します。以前の速度比較とは別に、今回は判定結果の違いを調べます。
...

---

*この記事は自動収集システムによって保存されました。*
