---
title: "エクスポート前にログをフィルター・整形・赤字化するためのTransforms"
source: "Cloudflare Blog"
category: "it"
published: 2026-10-12T14:44:59
url: https://blog.cloudflare.com/transformers-on-logpush/
---

# エクスポート前にログをフィルター・整形・赤字化するためのTransforms

## メタデータ

- **情報源**: Cloudflare Blog
- **カテゴリ**: it
- **公開日時**: 2026年10月12日 14:44
- **URL**: [https://blog.cloudflare.com/transformers-on-logpush/](https://blog.cloudflare.com/transformers-on-logpush/)

## 概要

Logpushは現在Transformersをサポートしており、SQLを使ってエクスポート前にログストリームをフィルタリング・ redact（秘匿）・再構成することができます。Apache DataFusionとApache Arrowを核として動作するTransformersは、目的地に到達する前にログデータ自体にこれらの変更を直接適用します。

---

*この記事は自動収集システムによって保存されました。*
