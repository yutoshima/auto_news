---
title: "ドメインモデル実装におけるトリレンマに対するSoutherの回答"
source: "Zenn"
category: "it"
published: 2026-09-10T01:11:08
url: https://zenn.dev/kawasima/articles/souther-ddd-trilemma
---

# ドメインモデル実装におけるトリレンマに対するSoutherの回答

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月10日 01:11
- **URL**: [https://zenn.dev/kawasima/articles/souther-ddd-trilemma](https://zenn.dev/kawasima/articles/souther-ddd-trilemma)

## 概要

ドメインモデル貧血症はなぜ生まれるのか — Decision パターンで DDD トリレンマを解く は Domain model purity vs. domain model completeness (DDD Trilemma)を非常に分かりやすく解説し、かつGoでこの循環を解消する方法として、domainの関数が「許可」「拒否」「まだ終わっていない、これを取ってきてほしい」の3種類を返すDecisionパターンを示している良い記事だと思いました。

ただ、Decisionパターンはやはり実装上の課題をドメインモデルに持ち込んでしまうので、外部I/Oをdomainの外に置ける一方、決...

---

*この記事は自動収集システムによって保存されました。*
