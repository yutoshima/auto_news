---
title: "AWS Global Acceleratorは、TLSリスナーを持つNLBに対してクライアントIPを保持します"
source: "AWS What's New"
category: "it"
published: 2026-11-23T16:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/global-accelerator-client-ip-nlb-tls/
---

# AWS Global Acceleratorは、TLSリスナーを持つNLBに対してクライアントIPを保持します

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 16:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/global-accelerator-client-ip-nlb-tls/](https://aws.amazon.com/about-aws/whats-new/2026/11/global-accelerator-client-ip-nlb-tls/)

## 概要

AWS Global Acceleratorは、TLSリスナーを使用するNLB（Network Load Balancer）エンドポイントへのトラフィックについて、クライアントIPアドレスを保持するようになりました。NLBでTLSを終了しても、アプリケーションで元のクライアントIPアドレスを確認できます。これにより、実際のクライアントIPに基づいて、セキュリティグループ、Geoブロック、レートリミティング、不正検知、監査ログ、許可リスト、コンプライアンス管理を適用できます。

以前は、TLSリスナーを持つNLBを、Acceleratorに追加することができませんでしたが…

---

*この記事は自動収集システムによって保存されました。*
