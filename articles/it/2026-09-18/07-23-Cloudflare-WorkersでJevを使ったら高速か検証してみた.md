---
title: "Cloudflare WorkersでJevを使ったら高速か検証してみた"
source: "Zenn"
category: "it"
published: 2026-09-18T07:23:34
url: https://zenn.dev/henteko/articles/1d159d10413312
---

# Cloudflare WorkersでJevを使ったら高速か検証してみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月18日 07:23
- **URL**: [https://zenn.dev/henteko/articles/1d159d10413312](https://zenn.dev/henteko/articles/1d159d10413312)

## 概要

結論

Cloudflare Workers上でJevのAPIを直接使うのが最速
Cloudflare AI Gateway経由で使う場合AI Gateway経由分遅くなる
クライアントが日本な限りレイテンシは遅くなってしまう


 はじめに
Cloudflare AI Gatewayでみんな大好きJevが使えるようになったので使ってみました。
https://developers.cloudflare.com/ai/models/typesafe/jev/
Jevの特徴としては「とにかく高速」ということなんですが、Jevのサーバーがアメリカの西海岸(Oregon)にあるらしく、日本...

---

*この記事は自動収集システムによって保存されました。*
