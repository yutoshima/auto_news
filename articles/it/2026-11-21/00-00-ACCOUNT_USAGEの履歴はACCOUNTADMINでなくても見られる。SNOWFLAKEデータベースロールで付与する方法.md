---
title: "ACCOUNT_USAGEの履歴はACCOUNTADMINでなくても見られる。SNOWFLAKEデータベースロールで付与する方法"
source: "DevelopersIO"
category: "it"
published: 2026-11-21T00:00:11
url: https://dev.classmethod.jp/articles/snowflake-database-role-system-views/
---

# ACCOUNT_USAGEの履歴はACCOUNTADMINでなくても見られる。SNOWFLAKEデータベースロールで付与する方法

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月21日 00:00
- **URL**: [https://dev.classmethod.jp/articles/snowflake-database-role-system-views/](https://dev.classmethod.jp/articles/snowflake-database-role-system-views/)

## 概要

Snowflakeのクエリ履歴やクレジット確認をACCOUNTADMINでしか行えないと思い込んでいませんか？実は、SNOWFLAKEデータベースロールを付与すれば、ACCOUNTADMIN以外のロールでもアカウント使用状況のビューを読めるようになります。その方法と設定方法を解説します。

---

*この記事は自動収集システムによって保存されました。*
