---
title: "Object.freezeで設定を守るときの境界：入れ子の書き換えとstrict modeをNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-14T01:06:26
url: https://qiita.com/ennagara128/items/38a85fe8a9fb8da6ce40
---

# Object.freezeで設定を守るときの境界：入れ子の書き換えとstrict modeをNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月14日 01:06
- **URL**: [https://qiita.com/ennagara128/items/38a85fe8a9fb8da6ce40](https://qiita.com/ennagara128/items/38a85fe8a9fb8da6ce40)

## 概要

Object.freeze() が守る階層と、代入時の例外を実測しました。
macOS 27.2 / Node.js v24.22.1で各例を .mjs に保存して実測。ブラウザ・Windows・型検査は未検証です。

外側の代入は止まり、内側の代入は通る
const se...

---

*この記事は自動収集システムによって保存されました。*
