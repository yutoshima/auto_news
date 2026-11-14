---
title: "dbtとSnowflakeでデータモデリング：顧客の履歴とID変更を題材にDimension Surrogate KeyとDurable Keyの違いを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-13T05:40:04
url: https://dev.classmethod.jp/articles/dbt-snowflake-modeling-dimension-surrogate-and-durable-key/
---

# dbtとSnowflakeでデータモデリング：顧客の履歴とID変更を題材にDimension Surrogate KeyとDurable Keyの違いを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月13日 05:40
- **URL**: [https://dev.classmethod.jp/articles/dbt-snowflake-modeling-dimension-surrogate-and-durable-key/](https://dev.classmethod.jp/articles/dbt-snowflake-modeling-dimension-surrogate-and-durable-key/)

## 概要

dbt Projects on SnowflakeでKimballのDimension Surrogate KeyとDurable Keyを実装して、顧客IDの再発行や会員ランク変更に対応したデータモデリングを試してみました。受注分析で注文時点の属性と現在の属性を使い分けるための2つのキーの違いと使い方を、実例で紹介します。

---

*この記事は自動収集システムによって保存されました。*
