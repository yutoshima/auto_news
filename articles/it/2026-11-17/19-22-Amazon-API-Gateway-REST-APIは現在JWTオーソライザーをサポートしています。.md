---
title: "Amazon API Gateway REST APIは現在JWTオーソライザーをサポートしています。"
source: "AWS What's New"
category: "it"
published: 2026-11-17T19:22:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-api-gateway-rest-authorizers-jwt/
---

# Amazon API Gateway REST APIは現在JWTオーソライザーをサポートしています。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月17日 19:22
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-api-gateway-rest-authorizers-jwt/](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-api-gateway-rest-authorizers-jwt/)

## 概要

<p>Amazon API Gatewayは現在、REST API용のネイティブJWT認証者を提供しています。ゲートウェイ自体でJSON Web Tokenを直接検証する新しい認証者タイプです。これまでは、OpenID ConnectまたはOAuth 2.0のアイデンティティプロバイダ（Amazon Cognito以外）からのトークンを検証するにはLambda認証者が必要でした。これからは、トークンの検証をコードの作成や運用に代えて、検証の設定を行います。</p> 
<p>発行者を1つ以上定義し、それぞれが受け付けるオーディエンス、許可する署名アルゴリズム、その他の設定を指定できます。</p>

---

*この記事は自動収集システムによって保存されました。*
