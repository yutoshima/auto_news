---
title: "React 18以降はFCはchildrenを暗黙的に型に含めない"
source: "Qiita (React)"
category: "it"
published: 2026-06-25T21:46:56
url: https://qiita.com/kusanishi/items/ef1f17433d6ce60a5268
---

# React 18以降はFCはchildrenを暗黙的に型に含めない

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年06月25日 21:46
- **URL**: [https://qiita.com/kusanishi/items/ef1f17433d6ce60a5268](https://qiita.com/kusanishi/items/ef1f17433d6ce60a5268)

## 概要

はじめに
TypeScript 学習中にFCを使って関数に型定義をしたが、childrenを渡した時にエラーとなった。

原因
React.FC は children を暗黙的に持つ挙動だと思っていたがReact 18以降は children をもたなくなったみたい。
 ...

---

*この記事は自動収集システムによって保存されました。*
