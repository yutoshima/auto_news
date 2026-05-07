---
title: "AIのPlan Modeをなんとなく承認しないために"
source: "Zenn"
category: "it"
published: 2026-05-07T00:30:01
url: https://zenn.dev/lv/articles/9438e1678c873a
---

# AIのPlan Modeをなんとなく承認しないために

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月07日 00:30
- **URL**: [https://zenn.dev/lv/articles/9438e1678c873a](https://zenn.dev/lv/articles/9438e1678c873a)

## 概要

TL;DR

Plan Modeでも、Planを承認してよいかを判断する基準は人間側に必要
その基準として、まず受け入れ条件を整理し、Planがそれを満たす内容かを見る
AIには受け入れ条件を決めさせず、既存情報から候補を抽出させ、人間が根拠つきで整理する
最後はAIの「🤖 完了しました」ではなく、当初の受け入れ条件を満たしたかで判断する


 Plan Modeは便利だけど、そのPlanの正しさは別問題
Claude CodeやCodexで実装するとき、Plan Modeを使う場面が増えてきました。
いきなりファイルを書き換えられるより、先に実装計画を出してもらえるほうが安心です。...

---

*この記事は自動収集システムによって保存されました。*
