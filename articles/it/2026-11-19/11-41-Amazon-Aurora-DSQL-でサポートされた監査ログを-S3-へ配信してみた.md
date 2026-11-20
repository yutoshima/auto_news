---
title: "Amazon Aurora DSQL でサポートされた監査ログを S3 へ配信してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T11:41:47
url: https://dev.classmethod.jp/articles/aurora-dsql-audit-logging-s3-delivery/
---

# Amazon Aurora DSQL でサポートされた監査ログを S3 へ配信してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 11:41
- **URL**: [https://dev.classmethod.jp/articles/aurora-dsql-audit-logging-s3-delivery/](https://dev.classmethod.jp/articles/aurora-dsql-audit-logging-s3-delivery/)

## 概要

Amazon Aurora DSQL の監査ログを S3 へ配信し、記録される SQL 文とレコードの内容を確かめました。実行から S3 に届くまでの時間は81〜342秒（6回の測定）で、READ と WRITE のレコードにはテーブル名の項目が入りませんでした。設定変更の反映は、約6分後にも新規接続で旧設定が適用されることがありました。

---

*この記事は自動収集システムによって保存されました。*
