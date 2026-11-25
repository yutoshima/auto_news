---
title: "Promise.allSettledでも全件成功とは限らない：結果・順序・同期例外の3点をNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-25T01:53:05
url: https://qiita.com/ennagara128/items/8a538a30e9ed8c000668
---

# Promise.allSettledでも全件成功とは限らない：結果・順序・同期例外の3点をNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 01:53
- **URL**: [https://qiita.com/ennagara128/items/8a538a30e9ed8c000668](https://qiita.com/ennagara128/items/8a538a30e9ed8c000668)

## 概要

Promise.allSettled() を待って catch に入らなくても、全件成功とは限りません。
入力の Promise が reject しても、全体は fulfilled になります。次の3点を点検します。
実測環境は macOS 27.2.1 / Node.j...

---

*この記事は自動収集システムによって保存されました。*
