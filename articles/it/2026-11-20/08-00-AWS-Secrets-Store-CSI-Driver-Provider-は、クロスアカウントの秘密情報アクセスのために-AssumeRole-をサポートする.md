---
title: "AWS Secrets Store CSI Driver Provider は、クロスアカウントの秘密情報アクセスのために AssumeRole をサポートするようになりました"
source: "AWS What's New"
category: "it"
published: 2026-11-20T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-store-csi-driver-assumerole/
---

# AWS Secrets Store CSI Driver Provider は、クロスアカウントの秘密情報アクセスのために AssumeRole をサポートするようになりました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-store-csi-driver-assumerole/](https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-store-csi-driver-assumerole/)

## 概要

<p>AWS Secrets Store CSI Driver Providerは現在、AssumeRole（ロールチェーン）をサポートしており、Kubernetesポッドが秘密情報を保存しているアカウントでIAMロールを引き受けることで、AWSアカウント間で秘密情報やパラメータへアクセスできるようになりました。以前は、クロスアカウントの秘密情報を読み取るには、各秘密情報にリソースポリシーを追加し、顧客管理のKMSキーを使用する必要がありました。なぜなら、AWSマネージドキー（aws/secretsmanager）はクロスアカウントアクセスには使用できなかったからです。今では、Secret内のターゲットロールを指定することで、チームは...</p>

---

*この記事は自動収集システムによって保存されました。*
