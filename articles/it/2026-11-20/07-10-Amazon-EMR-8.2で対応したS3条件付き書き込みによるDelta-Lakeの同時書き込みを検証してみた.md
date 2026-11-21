---
title: "Amazon EMR 8.2で対応したS3条件付き書き込みによるDelta Lakeの同時書き込みを検証してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T07:10:31
url: https://dev.classmethod.jp/articles/emr-8-2-delta-lake-concurrent/
---

# Amazon EMR 8.2で対応したS3条件付き書き込みによるDelta Lakeの同時書き込みを検証してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 07:10
- **URL**: [https://dev.classmethod.jp/articles/emr-8-2-delta-lake-concurrent/](https://dev.classmethod.jp/articles/emr-8-2-delta-lake-concurrent/)

## 概要

Amazon EMR 8.2がリリースされ、DynamoDBなしでS3上のDelta Lakeテーブルへ複数クラスターから安全に同時書き込みできるようになりました。検証環境の構築と、実際にS3の条件付き書き込みを活用した同時INSERT・MERGE処理を検証してみました。

---

*この記事は自動収集システムによって保存されました。*
