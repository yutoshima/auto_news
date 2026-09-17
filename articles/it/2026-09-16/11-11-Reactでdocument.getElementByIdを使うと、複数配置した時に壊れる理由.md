---
title: "Reactでdocument.getElementByIdを使うと、複数配置した時に壊れる理由"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-09-16T11:11:59
url: https://qiita.com/ennagara128/items/47d75576b3aff608b4f9
---

# Reactでdocument.getElementByIdを使うと、複数配置した時に壊れる理由

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年09月16日 11:11
- **URL**: [https://qiita.com/ennagara128/items/47d75576b3aff608b4f9](https://qiita.com/ennagara128/items/47d75576b3aff608b4f9)

## 概要

Reactのコンポーネントの中で、DOMの要素を直接書き換えたいとき、document.getElementByIdを使ったコードを見かけることがあります。単体では動いてしまうため気づきにくいのですが、同じコンポーネントを2つ以上並べた瞬間に壊れます。

Before: d...

---

*この記事は自動収集システムによって保存されました。*
