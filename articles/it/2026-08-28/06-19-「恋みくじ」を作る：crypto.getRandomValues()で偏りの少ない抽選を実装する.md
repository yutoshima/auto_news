---
title: "「恋みくじ」を作る：crypto.getRandomValues()で偏りの少ない抽選を実装する"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-28T06:19:56
url: https://qiita.com/izenndo/items/ef343216d032d79a7c3c
---

# 「恋みくじ」を作る：crypto.getRandomValues()で偏りの少ない抽選を実装する

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月28日 06:19
- **URL**: [https://qiita.com/izenndo/items/ef343216d032d79a7c3c](https://qiita.com/izenndo/items/ef343216d032d79a7c3c)

## 概要

Webブラウザだけで動く、小さな「恋みくじ」を作ります。
単に配列からランダムに1件選ぶだけなら数行で書けますが、この記事では次の点まで考えます。

Math.random()に頼らずWeb Crypto APIを使う
剰余（%）による偏りを避ける
結果をtextCont...

---

*この記事は自動収集システムによって保存されました。*
