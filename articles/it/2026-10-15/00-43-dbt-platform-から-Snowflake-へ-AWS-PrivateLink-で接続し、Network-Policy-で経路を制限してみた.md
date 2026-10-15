---
title: "dbt platform から Snowflake へ AWS PrivateLink で接続し、Network Policy で経路を制限してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-15T00:43:26
url: https://dev.classmethod.jp/articles/dbt-platform-snowflake-aws-privatelink-network-policy/
---

# dbt platform から Snowflake へ AWS PrivateLink で接続し、Network Policy で経路を制限してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 00:43
- **URL**: [https://dev.classmethod.jp/articles/dbt-platform-snowflake-aws-privatelink-network-policy/](https://dev.classmethod.jp/articles/dbt-platform-snowflake-aws-privatelink-network-policy/)

## 概要

dbt platformからSnowflakeへのAWS PrivateLink接続を、自身の検証環境で設定してみました。Enterprise+プランの機能を使い、dbt側のVPC endpointを通った接続がSnowflake側のログで確認できるまでと、public接続を拒否するNetwork Policyの設定例をまとめています。

---

*この記事は自動収集システムによって保存されました。*
