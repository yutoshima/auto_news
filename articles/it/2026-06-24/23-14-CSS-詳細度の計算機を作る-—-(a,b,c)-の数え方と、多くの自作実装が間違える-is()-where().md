---
title: "CSS 詳細度の計算機を作る — (a,b,c) の数え方と、多くの自作実装が間違える :is() / :where()"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-06-24T23:14:52
url: https://qiita.com/sen-ltd/items/70b5f5617ebcd3fffd5b
---

# CSS 詳細度の計算機を作る — (a,b,c) の数え方と、多くの自作実装が間違える :is() / :where()

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年06月24日 23:14
- **URL**: [https://qiita.com/sen-ltd/items/70b5f5617ebcd3fffd5b](https://qiita.com/sen-ltd/items/70b5f5617ebcd3fffd5b)

## 概要

CSS セレクタの詳細度 (specificity) をトークンごとに分解して計算し、複数セレクタを並べて「どれが勝つか」を判定するツールを作った。詳細度は (a, b, c) の 3 つ組で、一見「ID・class・要素を数えるだけ」に見える。だが実装の hinge は...

---

*この記事は自動収集システムによって保存されました。*
