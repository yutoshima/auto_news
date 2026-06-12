---
title: "notFound() を呼んでいるのに 200 が返ってくる — 62万ページのサイトで踏んだ Next.js loading.tsx の罠"
source: "Qiita (React)"
category: "it"
published: 2026-06-11T21:36:32
url: https://qiita.com/av_shiritai/items/c31cd6a411f038dd5add
---

# notFound() を呼んでいるのに 200 が返ってくる — 62万ページのサイトで踏んだ Next.js loading.tsx の罠

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年06月11日 21:36
- **URL**: [https://qiita.com/av_shiritai/items/c31cd6a411f038dd5add](https://qiita.com/av_shiritai/items/c31cd6a411f038dd5add)

## 概要

運営しているサイト(Next.js / App Router / 約62万ページ)で、低品質ページを notFound() で 404 化する変更をデプロイしたところ、notFound() は確実に実行されているのにレスポンスは 200 のまま、という現象にハマりました。
...

---

*この記事は自動収集システムによって保存されました。*
