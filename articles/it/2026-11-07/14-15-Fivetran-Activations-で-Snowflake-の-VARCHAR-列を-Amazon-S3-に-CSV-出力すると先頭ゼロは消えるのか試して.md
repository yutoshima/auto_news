---
title: "Fivetran Activations で Snowflake の VARCHAR 列を Amazon S3 に CSV 出力すると先頭ゼロは消えるのか試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-07T14:15:23
url: https://dev.classmethod.jp/articles/fivetran-activations-snowflake-varchar-s3-csv-leading-zeros/
---

# Fivetran Activations で Snowflake の VARCHAR 列を Amazon S3 に CSV 出力すると先頭ゼロは消えるのか試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月07日 14:15
- **URL**: [https://dev.classmethod.jp/articles/fivetran-activations-snowflake-varchar-s3-csv-leading-zeros/](https://dev.classmethod.jp/articles/fivetran-activations-snowflake-varchar-s3-csv-leading-zeros/)

## 概要

Fivetran Activations を使って、Snowflake の先頭ゼロ付き VARCHAR 列を S3 に出力する際、CSV / TSV / Parquet の 3 形式でデータがどう扱われるかを実検証してみました。

---

*この記事は自動収集システムによって保存されました。*
