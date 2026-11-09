---
title: "Amazon CloudWatch は現在、OpenTelemetry トレースの API キーをサポートしています"
source: "AWS What's New"
category: "it"
published: 2026-11-03T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-api-keys-opentelemetry/
---

# Amazon CloudWatch は現在、OpenTelemetry トレースの API キーをサポートしています

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-api-keys-opentelemetry/](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-api-keys-opentelemetry/)

## 概要

<p><a href="https://aws.amazon.com/cloudwatch/">Amazon CloudWatch</a>は現在、認証情報としてのAPIキー（ベアラートークン）を用いるベアラートークン認証をサポートしています。これを、AWS X-Ray OpenTelemetry Protocol（OTLP）トレース端点へOpenTelemetryトレースを送信する追加オプションとして利用できます。Authorizationヘッダーを設定できるすべてのOTLP/HTTPクライアント（OpenTelemetryコレクターやOpenTelemetry SDKのエクスポーターを含む）は、AWS Signature Version 4（SigV4）で署名する代わりに、ベアラートークンで認証できます。

---

*この記事は自動収集システムによって保存されました。*
