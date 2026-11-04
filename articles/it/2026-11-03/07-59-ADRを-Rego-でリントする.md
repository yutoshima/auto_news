---
title: "ADRを Rego でリントする"
source: "Zenn"
category: "it"
published: 2026-11-03T07:59:33
url: https://zenn.dev/babarot/articles/regomark-adr-checker
---

# ADRを Rego でリントする

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 07:59
- **URL**: [https://zenn.dev/babarot/articles/regomark-adr-checker](https://zenn.dev/babarot/articles/regomark-adr-checker)

## 概要

AIが書くADRのフォーマットをどう揃えるか
自分のリポジトリでは、設計の決定を ADR（Architecture Decision Records）として docs/adr/ に残している。最近は、その ADR の多くを Claude Code に書いてもらっている。決定を相談して、「これを ADR にしておいて」と頼むと書いてくれる。
ただ、AI に書かせた ADR は、少しずつ自由になっていく。テンプレートを置いて書き方を指示していても、ずれるときはずれる。たとえば、

Decision に、画面のメニュー項目の一覧や定数、構造体の定義まで書いてある。仕様書に近づいて、コードを...

---

*この記事は自動収集システムによって保存されました。*
