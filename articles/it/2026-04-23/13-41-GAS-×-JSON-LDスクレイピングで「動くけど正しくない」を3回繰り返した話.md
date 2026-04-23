---
title: "GAS × JSON-LDスクレイピングで「動くけど正しくない」を3回繰り返した話"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-04-23T13:41:51
url: https://qiita.com/freefreefree1222/items/2ca283db2a1ae40a4291
---

# GAS × JSON-LDスクレイピングで「動くけど正しくない」を3回繰り返した話

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年04月23日 13:41
- **URL**: [https://qiita.com/freefreefree1222/items/2ca283db2a1ae40a4291](https://qiita.com/freefreefree1222/items/2ca283db2a1ae40a4291)

## 概要

構造化データ（JSON-LD）が埋め込まれていれば楽勝だろう、と思って着手した求人サイトスクレイピング。結果として3回ハマって、最後は JSON.parse を捨てました。同じ罠を踏みそうな方の参考に、具体的なコード例と判断の流れを共有します。

環境

実行環境: Goo...

---

*この記事は自動収集システムによって保存されました。*
