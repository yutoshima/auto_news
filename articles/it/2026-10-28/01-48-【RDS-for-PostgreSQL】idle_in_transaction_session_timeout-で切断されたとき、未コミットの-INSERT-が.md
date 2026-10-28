---
title: "【RDS for PostgreSQL】idle_in_transaction_session_timeout で切断されたとき、未コミットの INSERT がどうなるか確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-28T01:48:17
url: https://dev.classmethod.jp/articles/rds-postgresql-idle-in-transaction-session-timeout-rollback/
---

# 【RDS for PostgreSQL】idle_in_transaction_session_timeout で切断されたとき、未コミットの INSERT がどうなるか確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 01:48
- **URL**: [https://dev.classmethod.jp/articles/rds-postgresql-idle-in-transaction-session-timeout-rollback/](https://dev.classmethod.jp/articles/rds-postgresql-idle-in-transaction-session-timeout-rollback/)

## 概要

RDS for PostgreSQL で idle_in_transaction_session_timeout を設定し、トランザクション中に放置した接続が切断されたとき、未コミットの INSERT がどうなるかを psql で確認してみました。

---

*この記事は自動収集システムによって保存されました。*
