---
title: "Strands BoxをEC2 Macで実測 — Dogwoodポリシーが効く経路を仕分け"
source: "Zenn"
category: "it"
published: 2026-10-11T14:12:08
url: https://zenn.dev/kashiwabaray/articles/fc2d097da71f30
---

# Strands BoxをEC2 Macで実測 — Dogwoodポリシーが効く経路を仕分け

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月11日 14:12
- **URL**: [https://zenn.dev/kashiwabaray/articles/fc2d097da71f30](https://zenn.dev/kashiwabaray/articles/fc2d097da71f30)

## 概要

1. はじめに
AI コーディングエージェントを、操作ごとの承認なしで動かす運用が増えています。そうした運用で問題になるのは、「どこまで触れるか」だけではありません。「触れてよいものに対して何をしてよいか」も決めておく必要があります。コンテナや microVM はアクセス範囲に境界を引けます。一方で「機密ファイルを読んだあとは特定の宛先への送信を禁止する」「Slack への投稿は10分に3回まで」のような、過去の操作履歴に応じたルールは別の仕組みで持つ必要があります。
2026/10/07 に、AWS（Amazon Web Services）が Strands Box を devel...

---

*この記事は自動収集システムによって保存されました。*
