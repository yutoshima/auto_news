---
title: "Cloudflare Workers + better-auth で全リクエストが無応答になる - hanging promise の罠"
source: "Zenn"
category: "it"
published: 2026-07-05T10:11:56
url: https://zenn.dev/coji/articles/cloudflare-workers-better-auth-hanging-promise
---

# Cloudflare Workers + better-auth で全リクエストが無応答になる - hanging promise の罠

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月05日 10:11
- **URL**: [https://zenn.dev/coji/articles/cloudflare-workers-better-auth-hanging-promise](https://zenn.dev/coji/articles/cloudflare-workers-better-auth-hanging-promise)

## 概要

これはなに？
Cloudflare Workers + D1 + better-auth で運用している Web サービスで、「特定のユーザーだけ、サイトへの全リクエストが応答待ちのまま固まり、ブラウザを再起動しないと直らない」という障害に繰り返し遭遇しました。丸一日かけて原因を特定して解決したので、同じ構成でハマった人が解決策にたどり着けるように、調査の過程と修正をまとめておきます。
原因は Cloudflare Workers の hanging promise でした。リクエスト処理中に生成された promise は、そのリクエストがクライアントに中断されると永遠に解決しなくな...

---

*この記事は自動収集システムによって保存されました。*
