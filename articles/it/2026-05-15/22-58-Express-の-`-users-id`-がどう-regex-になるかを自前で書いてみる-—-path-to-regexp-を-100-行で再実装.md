---
title: "Express の `/users/:id` がどう regex になるかを自前で書いてみる — path-to-regexp を 100 行で再実装"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-05-15T22:58:00
url: https://qiita.com/sen-ltd/items/99c119dbc2980e077602
---

# Express の `/users/:id` がどう regex になるかを自前で書いてみる — path-to-regexp を 100 行で再実装

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年05月15日 22:58
- **URL**: [https://qiita.com/sen-ltd/items/99c119dbc2980e077602](https://qiita.com/sen-ltd/items/99c119dbc2980e077602)

## 概要

app.get('/users/:id', ...) を Express に渡すと、内部で path-to-regexp が /^\/users\/([^/]+)$/ に変換している。これを自分で書いてみるとどう難しいか。? 修飾子と inline regex (:id(...

---

*この記事は自動収集システムによって保存されました。*
