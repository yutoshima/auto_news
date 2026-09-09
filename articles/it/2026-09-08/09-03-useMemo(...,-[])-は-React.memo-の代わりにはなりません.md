---
title: "useMemo(..., []) は React.memo の代わりにはなりません"
source: "Qiita (React)"
category: "it"
published: 2026-09-08T09:03:20
url: https://qiita.com/shun123/items/efa620d796000962fa63
---

# useMemo(..., []) は React.memo の代わりにはなりません

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年09月08日 09:03
- **URL**: [https://qiita.com/shun123/items/efa620d796000962fa63](https://qiita.com/shun123/items/efa620d796000962fa63)

## 概要

はじめに
Reactのレンダリング最適化で、React.memoの代わりにReact.useMemoを使ったらダメな理由を厳密に理解できていなかったのでこの記事をかきました。
例えば、こんなコードを見かけたことはないでしょうか？
export const Child: R...

---

*この記事は自動収集システムによって保存されました。*
