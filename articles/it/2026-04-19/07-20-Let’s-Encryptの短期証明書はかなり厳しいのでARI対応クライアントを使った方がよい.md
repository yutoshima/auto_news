---
title: "Let’s Encryptの短期証明書はかなり厳しいのでARI対応クライアントを使った方がよい"
source: "Zenn"
category: "it"
published: 2026-04-19T07:20:14
url: https://zenn.dev/catatsuy/articles/2ac24bccb4b7d1
---

# Let’s Encryptの短期証明書はかなり厳しいのでARI対応クライアントを使った方がよい

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月19日 07:20
- **URL**: [https://zenn.dev/catatsuy/articles/2ac24bccb4b7d1](https://zenn.dev/catatsuy/articles/2ac24bccb4b7d1)

## 概要

Let’s Encryptの短期証明書は、90日証明書の延長くらいの感覚で入るとかなり厳しいです。
サブドメインを含む複数の証明書を短い間隔で発行・更新する構成では、証明書発行まわりのレート制限に引っかかりやすくなります。短期証明書では更新回数が増えるので、その影響がかなり表面化しやすくなります。
https://letsencrypt.org/docs/rate-limits/

 まずステージング環境で試した方がよい
開発やテストでは、本番ではなくステージング環境を使った方がよいです。本番と同じ種類の挙動をかなり緩い制限で試せるので、証明書の切り方や更新方法を確認する段階では先にこち...

---

*この記事は自動収集システムによって保存されました。*
