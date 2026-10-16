---
title: "VPC origin がデュアルスタックをサポート。CloudFrontのオリジンリクエストが ALB まで IPv6 で届くか試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-15T23:05:22
url: https://dev.classmethod.jp/articles/aws-cloudfront-vpc-origin-dualstack/
---

# VPC origin がデュアルスタックをサポート。CloudFrontのオリジンリクエストが ALB まで IPv6 で届くか試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 23:05
- **URL**: [https://dev.classmethod.jp/articles/aws-cloudfront-vpc-origin-dualstack/](https://dev.classmethod.jp/articles/aws-cloudfront-vpc-origin-dualstack/)

## 概要

CloudFront VPC origin のデュアルスタック対応を、internal ALB への IPv6 接続で検証しました。VPC には通常の IGW が必要ですが、サブネットの IPv6 デフォルトルートを Egress-only IGW に向けた構成で作成できます。

---

*この記事は自動収集システムによって保存されました。*
