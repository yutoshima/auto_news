---
title: "Amazon S3 の PQ-TLS を CloudTrail のログ記録（keyExchange）で確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T14:59:00
url: https://dev.classmethod.jp/articles/amazon-s3-pq-tls-cloudtrail-key-exchange/
---

# Amazon S3 の PQ-TLS を CloudTrail のログ記録（keyExchange）で確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 14:59
- **URL**: [https://dev.classmethod.jp/articles/amazon-s3-pq-tls-cloudtrail-key-exchange/](https://dev.classmethod.jp/articles/amazon-s3-pq-tls-cloudtrail-key-exchange/)

## 概要

Amazon S3 のリクエストごとの TLS 鍵交換方式が CloudTrail の tlsDetails.keyExchange に記録されるようになりました。curl で固定した鍵交換と CloudTrail の値は一致し、AWS CLI の Docker イメージは版によって値が分かれました。

---

*この記事は自動収集システムによって保存されました。*
