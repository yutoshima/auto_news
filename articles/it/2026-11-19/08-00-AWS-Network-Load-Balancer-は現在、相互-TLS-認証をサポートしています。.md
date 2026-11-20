---
title: "AWS Network Load Balancer は現在、相互 TLS 認証をサポートしています。"
source: "AWS What's New"
category: "it"
published: 2026-11-19T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/network-load-balancer-mtls/
---

# AWS Network Load Balancer は現在、相互 TLS 認証をサポートしています。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/network-load-balancer-mtls/](https://aws.amazon.com/about-aws/whats-new/2026/11/network-load-balancer-mtls/)

## 概要

AWS Network Load Balancer（NLB）は、X.509証明書を提示するクライアントに対する相互TLS（mTLS）認証をサポートするようになりました。これまではNLBでmTLSを必要とする顧客は独自のソリューションを構築するか、クライアント認証のためにサードパーティのプロキシを使用していました。今回のリリースにより、NLBはTLSリスナー上でクライアント証明書を検証するため、信頼されたクライアントだけがターゲットへ到達できます。mTLS認証に必要な計算集約的な処理をNLBにオフロードできるため、証明書ロジックを自分側に追加する必要がありません。

---

*この記事は自動収集システムによって保存されました。*
