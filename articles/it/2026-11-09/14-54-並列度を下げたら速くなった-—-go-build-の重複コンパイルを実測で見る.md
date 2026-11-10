---
title: "並列度を下げたら速くなった — go build の重複コンパイルを実測で見る"
source: "はてブ テクノロジー"
category: "it"
published: 2026-11-09T14:54:51
url: https://speakerdeck.com/tomoaki25/slides-cd95d381-a27b-4a9a-8b53-0abd69397a1b
---

# 並列度を下げたら速くなった — go build の重複コンパイルを実測で見る

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年11月09日 14:54
- **URL**: [https://speakerdeck.com/tomoaki25/slides-cd95d381-a27b-4a9a-8b53-0abd69397a1b](https://speakerdeck.com/tomoaki25/slides-cd95d381-a27b-4a9a-8b53-0abd69397a1b)

## 概要

バクラクの monorepo で、同時に走らせる go build を 9 → 2 に減らしたら、起動時のビルドが 2.4 倍速くなりました。-debug-actiongraph でビルドの中を覗き、重複コンパイルが起きる理由と、さらに速くする方法を実測で紹介します。 layerx.go #6（2…

---

*この記事は自動収集システムによって保存されました。*
