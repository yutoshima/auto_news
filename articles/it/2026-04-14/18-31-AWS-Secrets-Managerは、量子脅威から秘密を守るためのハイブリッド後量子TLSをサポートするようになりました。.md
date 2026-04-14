---
title: "AWS Secrets Managerは、量子脅威から秘密を守るためのハイブリッド後量子TLSをサポートするようになりました。"
source: "AWS What's New"
category: "it"
published: 2026-04-14T18:31:00
url: https://aws.amazon.com/about-aws/whats-new/2026/04/aws-secrets-manager-post-quantum-tls/
---

# AWS Secrets Managerは、量子脅威から秘密を守るためのハイブリッド後量子TLSをサポートするようになりました。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年04月14日 18:31
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/04/aws-secrets-manager-post-quantum-tls/](https://aws.amazon.com/about-aws/whats-new/2026/04/aws-secrets-manager-post-quantum-tls/)

## 概要

AWS Secrets Manager は現在、TLS 接続のセキュリティを強化するために、ML-KEM（モジュール lattice ベースの鍵導出機構）を用いたハイブリッド後量子鍵交換をサポートしています。Secretの取得と管理を行う際のこの保護機能は、Secrets Manager Agent（バージョン 2.0.0 以降）、AWS Lambda Extension（バージョン 19 以降）、および Secrets Manager CSI Driver（バージョン 2.0.0 以降）で自動的に有効化されます。SDK ベースのクライアントでは、Rust、Go、Node.js、Kotli などを含む対応 AWS SDK でハイブリッド後量子鍵交換が利用可能です。

---

*この記事は自動収集システムによって保存されました。*
