---
title: "アイコンだけのボタンはaxeを素通りする - jsdomの単体テストにaxe-coreを直接組み込み、独自ルールで穴を埋める"
source: "Qiita (React)"
category: "it"
published: 2026-10-24T01:01:09
url: https://qiita.com/zucky-quest/items/f7215d4df9ebf857275c
---

# アイコンだけのボタンはaxeを素通りする - jsdomの単体テストにaxe-coreを直接組み込み、独自ルールで穴を埋める

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 01:01
- **URL**: [https://qiita.com/zucky-quest/items/f7215d4df9ebf857275c](https://qiita.com/zucky-quest/items/f7215d4df9ebf857275c)

## 概要

TL;DR

React の単体テスト（Vitest + jsdom）に、a11y（アクセシビリティ）の自動検査ツール axe を組み込みました
定番の vitest-axe は使わず、axe-core を直接呼ぶ約 100 行のヘルパーを作りました。保守が止まっていて、...

---

*この記事は自動収集システムによって保存されました。*
