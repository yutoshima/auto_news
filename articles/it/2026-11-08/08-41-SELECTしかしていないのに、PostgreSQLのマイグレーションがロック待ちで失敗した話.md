---
title: "SELECTしかしていないのに、PostgreSQLのマイグレーションがロック待ちで失敗した話"
source: "Zenn"
category: "it"
published: 2026-11-08T08:41:46
url: https://zenn.dev/naokisuzuki27/articles/cb1a5ac0e23763
---

# SELECTしかしていないのに、PostgreSQLのマイグレーションがロック待ちで失敗した話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月08日 08:41
- **URL**: [https://zenn.dev/naokisuzuki27/articles/cb1a5ac0e23763](https://zenn.dev/naokisuzuki27/articles/cb1a5ac0e23763)

## 概要

前提

DB：Amazon Aurora PostgreSQL 16


 TL;DR

SELECTしかしていないトランザクションが放置され、リリース時のマイグレーションがロック待ちで失敗した
PostgreSQLのロックは「共有」「排他」の2種類ではなく、SELECTが取るACCESS SHAREは REINDEX などが要求するACCESS EXCLUSIVEを止める
トランザクションは最小限に分け、保険としてAuroraの idle_in_transaction_session_timeout を設定した


 結論


ロックは「共有」と「排他」の2種類ではない：SELEC...

---

*この記事は自動収集システムによって保存されました。*
