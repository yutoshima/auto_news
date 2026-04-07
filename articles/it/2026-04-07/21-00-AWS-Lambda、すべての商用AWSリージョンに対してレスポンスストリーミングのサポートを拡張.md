---
title: "AWS Lambda、すべての商用AWSリージョンに対してレスポンスストリーミングのサポートを拡張"
source: "AWS What's New"
category: "it"
published: 2026-04-07T21:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/04/aws-lambda-response-streaming/
---

# AWS Lambda、すべての商用AWSリージョンに対してレスポンスストリーミングのサポートを拡張

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年04月07日 21:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/04/aws-lambda-response-streaming/](https://aws.amazon.com/about-aws/whats-new/2026/04/aws-lambda-response-streaming/)

## 概要

AWS Lambda のレスポンスストリーミングがすべての商用 AWS リージョンで利用可能になり、この機能のリージョン全体での同等性が実現しました。新たにサポートされたリージョンの顧客は InvokeWithResponseStream API を使用して、データが利用可能になるたびにクライアントへ段階的にレスポンスペイロードをストリーミングできます。

レスポンスストリーミングにより、関数は送信前に全体のレスポンスをバッファするのではなく、クライアントへ部分的なレスポンスを順次送信できるようになります。これにより、初回バイトまでの待機時間（TTFB）しかつぽの遅延を低減します。

---

*この記事は自動収集システムによって保存されました。*
