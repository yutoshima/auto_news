---
title: "AWS Secrets Store CSI Driver Provider は、クロスアカウントの秘密アクセスのための AssumeRole をサポートしました"
source: "AWS What's New"
category: "it"
published: 2026-11-20T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-store-csi-driver-assumerole/
---

# AWS Secrets Store CSI Driver Provider は、クロスアカウントの秘密アクセスのための AssumeRole をサポートしました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-store-csi-driver-assumerole/](https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-store-csi-driver-assumerole/)

## 概要

<p> AWS Secrets Store CSI Driver Provider は現在 AssumeRole（ロール連鎖）をサポートしており、Kubernetes ポッドがシークレットを格納している AWS アカウント内の IAM ロールを引き受けることで、別の AWS アカウントのシークレットやパラメータへアクセスできるようになりました。以前は、クロスアカウントのシークレットを読み取る場合、各シークレットにリソースポリシーを追加し、顧客管理の KMS キーを使用する必要がありました。AWS が管理するキー（aws/secretsmanager）はクロスアカウントアクセスには使用できないためです。 now, teams can name a target role in the Secret

---

*この記事は自動収集システムによって保存されました。*
