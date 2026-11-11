---
title: "Prop Drilling、そのまま使ってはいけないのか?"
source: "Qiita (React)"
category: "it"
published: 2026-11-10T11:50:26
url: https://qiita.com/gaeul0228/items/2fbbe5aa0798979219b2
---

# Prop Drilling、そのまま使ってはいけないのか?

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 11:50
- **URL**: [https://qiita.com/gaeul0228/items/2fbbe5aa0798979219b2](https://qiita.com/gaeul0228/items/2fbbe5aa0798979219b2)

## 概要

Reactで開発していると、一度はこんな場面に出会う。最上位のコンポーネントにあるstateを、ずっと下の深い階層にあるコンポーネントで使いたい。でも、その間にあるコンポーネントでは、その値をまったく使わない。
そのため、仕方なくpropsを一段ずつ渡していくことになる。こ...

---

*この記事は自動収集システムによって保存されました。*
