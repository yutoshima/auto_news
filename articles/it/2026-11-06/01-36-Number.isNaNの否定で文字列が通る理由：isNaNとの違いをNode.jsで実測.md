---
title: "Number.isNaNの否定で文字列が通る理由：isNaNとの違いをNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-06T01:36:59
url: https://qiita.com/ennagara128/items/20a66228e9424c28c6e1
---

# Number.isNaNの否定で文字列が通る理由：isNaNとの違いをNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月06日 01:36
- **URL**: [https://qiita.com/ennagara128/items/20a66228e9424c28c6e1](https://qiita.com/ennagara128/items/20a66228e9424c28c6e1)

## 概要

!Number.isNaN(value) は、数値の入力チェックとしては足りません。"abc" も null も通ります。number型の有限値だけを受け付けるなら、Number.isFinite(value) で確かめます。
2026年11月6日、macOS 27.2／N...

---

*この記事は自動収集システムによって保存されました。*
