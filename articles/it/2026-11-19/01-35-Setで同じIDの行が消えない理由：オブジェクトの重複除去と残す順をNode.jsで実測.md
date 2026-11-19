---
title: "Setで同じIDの行が消えない理由：オブジェクトの重複除去と残す順をNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-19T01:35:37
url: https://qiita.com/ennagara128/items/77b9ad11f6b7014a4ad7
---

# Setで同じIDの行が消えない理由：オブジェクトの重複除去と残す順をNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 01:35
- **URL**: [https://qiita.com/ennagara128/items/77b9ad11f6b7014a4ad7](https://qiita.com/ennagara128/items/77b9ad11f6b7014a4ad7)

## 概要

[...new Set(rows)] で一覧の重複を消したのに、同じ ID のデータが残る。オブジェクトの配列では、「同じ値」の意味を決める必要があります。
参照が同じ・ID が同じ・どの行を残すかを Q&amp;A で整理します。
検証環境は macOS 27.2.1、Node....

---

*この記事は自動収集システムによって保存されました。*
