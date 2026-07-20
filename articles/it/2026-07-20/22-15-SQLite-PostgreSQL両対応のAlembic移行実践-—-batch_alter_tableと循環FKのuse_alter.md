---
title: "SQLite/PostgreSQL両対応のAlembic移行実践 — batch_alter_tableと循環FKのuse_alter"
source: "Qiita (Python)"
category: "it"
published: 2026-07-20T22:15:36
url: https://qiita.com/ultimania/items/d6fc149b92a4316eb6e2
---

# SQLite/PostgreSQL両対応のAlembic移行実践 — batch_alter_tableと循環FKのuse_alter

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年07月20日 22:15
- **URL**: [https://qiita.com/ultimania/items/d6fc149b92a4316eb6e2](https://qiita.com/ultimania/items/d6fc149b92a4316eb6e2)

## 概要

「開発はSQLite、本番はPostgreSQL」という構成、便利ですよね。セットアップは軽いし、本番は堅牢。ただしこの構成には、マイグレーションで一度は踏む罠があります。
SQLiteは既存テーブルの制約変更(ALTER)ができません。 そのため、PostgreSQLでは...

---

*この記事は自動収集システムによって保存されました。*
