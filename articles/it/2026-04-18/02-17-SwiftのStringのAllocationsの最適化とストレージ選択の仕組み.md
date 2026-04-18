---
title: "SwiftのStringのAllocationsの最適化とストレージ選択の仕組み"
source: "Zenn"
category: "it"
published: 2026-04-18T02:17:06
url: https://zenn.dev/hinakko/articles/bfc446a24d0de0
---

# SwiftのStringのAllocationsの最適化とストレージ選択の仕組み

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月18日 02:17
- **URL**: [https://zenn.dev/hinakko/articles/bfc446a24d0de0](https://zenn.dev/hinakko/articles/bfc446a24d0de0)

## 概要

はじめに
try! Swift Tokyo2026のPaul HudsonさんのワークショップのHigh-Performance Swiftに参加し、Swift言語のStringStorageの話を聞き、Stringの内部構造とどのように最適化されているのかについて興味を持ったので、この記事を書きました。
https://x.com/hinakkograshi/status/2043153057278763029?s=20

 SwiftのStringのAllocations
Stringのストレージの格納場所は大きく分けて、Small String Optimization・__S...

---

*この記事は自動収集システムによって保存されました。*
