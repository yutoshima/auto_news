---
title: "本番でボタンが全部無反応だった——CSP の nonce と force-static は両立しない（Next.js App Router）"
source: "Qiita (React)"
category: "it"
published: 2026-09-29T00:58:09
url: https://qiita.com/sz_tak/items/bc1a124d90f1eac0c80a
---

# 本番でボタンが全部無反応だった——CSP の nonce と force-static は両立しない（Next.js App Router）

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年09月29日 00:58
- **URL**: [https://qiita.com/sz_tak/items/bc1a124d90f1eac0c80a](https://qiita.com/sz_tak/items/bc1a124d90f1eac0c80a)

## 概要

結論

Next.js App Router で、middleware がリクエストごとに nonce を発行する CSP（script-src 'self' 'nonce-…' 'strict-dynamic'）を使っていた
同じアプリの一部のページに export c...

---

*この記事は自動収集システムによって保存されました。*
