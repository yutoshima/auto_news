---
title: "Amazon DynamoDB の bulk put items で S3 のデータを既存テーブルへ登録してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-15T14:44:45
url: https://dev.classmethod.jp/articles/amazon-dynamodb-bulk-put-items/
---

# Amazon DynamoDB の bulk put items で S3 のデータを既存テーブルへ登録してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 14:44
- **URL**: [https://dev.classmethod.jp/articles/amazon-dynamodb-bulk-put-items/](https://dev.classmethod.jp/articles/amazon-dynamodb-bulk-put-items/)

## 概要

Amazon DynamoDB の bulk put items で、S3 の 10 KB のアイテムを100件から10万件まで東京リージョンの既存テーブルへ登録しました。全件が入り、所要時間は BatchWriteItem より長くなりました。入力を分けると短く、書き込み料金は試算で安くなりました。

---

*この記事は自動収集システムによって保存されました。*
