---
title: "EKS に Graviton を導入して、arm64 と amd64 を混ぜて運用を始めました"
source: "Zenn"
category: "it"
published: 2026-10-21T03:00:07
url: https://zenn.dev/socialplus/articles/eks-graviton-arm64-migration
---

# EKS に Graviton を導入して、arm64 と amd64 を混ぜて運用を始めました

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月21日 03:00
- **URL**: [https://zenn.dev/socialplus/articles/eks-graviton-arm64-migration](https://zenn.dev/socialplus/articles/eks-graviton-arm64-migration)

## 概要

こんにちは、ソーシャルPLUSの三口です!
弊社では Amazon EKS 上で Rails のアプリケーションを動かしていますが、これまでノードはすべて Intel/AMD (amd64) のインスタンスでした。今回、そのノードに AWS Graviton (arm64) を導入し、Spot インスタンスでは arm64 と amd64 を混ぜて運用する構成にしました。
Graviton への移行自体はすでに多くの企業が取り組んでいて、真新しい話ではないと思います。
ただ、4 月に入社した自分にとっては、インフラの知識だけでなく、各サービスがどう動いているかを知るきっかけにもなった案件...

---

*この記事は自動収集システムによって保存されました。*
