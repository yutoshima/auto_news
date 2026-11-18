---
title: "Amazon ECR は現在、プライベートレジストリ向けのグローバル認証トークンをサポートしています。"
source: "AWS What's New"
category: "it"
published: 2026-11-17T21:37:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/global-authentication-amazon-ecr
---

# Amazon ECR は現在、プライベートレジストリ向けのグローバル認証トークンをサポートしています。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月17日 21:37
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/global-authentication-amazon-ecr](https://aws.amazon.com/about-aws/whats-new/2026/11/global-authentication-amazon-ecr)

## 概要

Amazon Elastic Container Registry（Amazon ECR）は、プライベートレジストリ向けのグローバル認証トークンをサポートするようになりました。従来は、コンテナイメージのプッシュやプルを行う各AWSリージョンごとに別々の認証トークンを取得する必要がありました。 now、AWS Sign-In CreateBearerToken API から単一のトークンを取得し、同じAWSパーティション内のすべてのECRプライベートレジストリで利用できます。

リージョン間でコンテナのプルをルーティングするプロキシサービスを運用するチームにとっては、これは最適化のための一般的なパターンです。

---

*この記事は自動収集システムによって保存されました。*
