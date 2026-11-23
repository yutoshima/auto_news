---
title: "mizchi/mutator を入れてみた"
source: "Zenn"
category: "it"
published: 2026-11-16T03:49:18
url: https://zenn.dev/polyco/articles/e05cb28c569801
---

# mizchi/mutator を入れてみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月16日 03:49
- **URL**: [https://zenn.dev/polyco/articles/e05cb28c569801](https://zenn.dev/polyco/articles/e05cb28c569801)

## 概要

この記事に書いてあること

AI が書きまくったテストに意味のないテストがどれくらいあるのか数えた
金額や権限など間違えるとやばいところはテストの穴を 0 件にした
StrykerJS と条件をそろえて比べてみたけど確かに速い
開発ワークフロースキルに組み込んで、意味のないテストが書かれたらすぐ気づけるようにした
機械的に拾えないものはスキルでカバー
毎回全部は流さない。その作業で修正したコードとテストに関係するファイルだけ試す


 前提となる構成

Web も API も TypeScript で書いている 業務アプリ

pnpm workspaces でのモノレポ構成
Vite...

---

*この記事は自動収集システムによって保存されました。*
