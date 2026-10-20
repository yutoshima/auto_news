---
title: "AWS Lambda Web FunctionsでImpossible Location検知の課題をまとめて解決！ + 昨今の攻撃への有効性"
source: "Zenn"
category: "it"
published: 2026-10-19T04:08:01
url: https://zenn.dev/cscloud_blog/articles/f4ce99ffeb8ee3
---

# AWS Lambda Web FunctionsでImpossible Location検知の課題をまとめて解決！ + 昨今の攻撃への有効性

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月19日 04:08
- **URL**: [https://zenn.dev/cscloud_blog/articles/f4ce99ffeb8ee3](https://zenn.dev/cscloud_blog/articles/f4ce99ffeb8ee3)

## 概要

これまで下記の 2 本の記事で、Amazon CloudFront を使ってセッションハイジャックを検知・ブロックする仕組みを紹介してきました。


CloudFront Functions + KVS 編：エッジで高速に検証できる。ただしアプリ改修が必要で、KVS の 5MB 上限・TTL なし・結果整合と付き合う必要がある

Lambda@Edge 編：アプリ無改修。ただし署名付き Cookie なのでセッション単位の失効ができない

CloudFront Functions 編の最後で、

結論として、CloudFront Functions のエッジ完結という利点を活かすには K...

---

*この記事は自動収集システムによって保存されました。*
