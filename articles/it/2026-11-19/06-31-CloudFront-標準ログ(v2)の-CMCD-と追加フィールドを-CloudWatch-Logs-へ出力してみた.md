---
title: "CloudFront 標準ログ(v2)の CMCD と追加フィールドを CloudWatch Logs へ出力してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T06:31:14
url: https://dev.classmethod.jp/articles/cloudfront-standard-logging-cmcd-fields/
---

# CloudFront 標準ログ(v2)の CMCD と追加フィールドを CloudWatch Logs へ出力してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 06:31
- **URL**: [https://dev.classmethod.jp/articles/cloudfront-standard-logging-cmcd-fields/](https://dev.classmethod.jp/articles/cloudfront-standard-logging-cmcd-fields/)

## 概要

Amazon CloudFront の標準ログ(v2)で、CMCD と追加フィールドを CloudWatch Logs へ出力しました。どちらも --record-fields で指定すると出力され、CMCD のフィールドに値が入ったのは、curl でクエリまたはヘッダーに付けて送ったリクエストだけでした。

---

*この記事は自動収集システムによって保存されました。*
