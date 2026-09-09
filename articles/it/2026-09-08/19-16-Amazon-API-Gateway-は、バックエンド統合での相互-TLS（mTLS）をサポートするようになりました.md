---
title: "Amazon API Gateway は、バックエンド統合での相互 TLS（mTLS）をサポートするようになりました"
source: "AWS What's New"
category: "it"
published: 2026-09-08T19:16:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-mutual-tls-backend/
---

# Amazon API Gateway は、バックエンド統合での相互 TLS（mTLS）をサポートするようになりました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月08日 19:16
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-mutual-tls-backend/](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-mutual-tls-backend/)

## 概要

現在、Amazon API Gateway REST APIを構成して、TLSハンドシェイクの際にバックエンドへAWS Certificate Manager（ACM）証明書を提示し、相互TLS（mTLS）を有効にできます。従来、API Gatewayは自分で生成した自己署名証明書のみを提示していましたが、信頼できる認証局（CA）により署名された証明書を使用できるようになりました。統合エンドポイントはハンドシェイク中にこの証明書を検証し、接続元があなたのAPIであることを確認します。

---

*この記事は自動収集システムによって保存されました。*
