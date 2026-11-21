---
title: "[アップデート] Amazon S3 Tables のレプリカを書き込み可能なテーブルに昇格できるようになったので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T17:12:58
url: https://dev.classmethod.jp/articles/20261120-amazon-s3-tables-replication-writable-tables/
---

# [アップデート] Amazon S3 Tables のレプリカを書き込み可能なテーブルに昇格できるようになったので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 17:12
- **URL**: [https://dev.classmethod.jp/articles/20261120-amazon-s3-tables-replication-writable-tables/](https://dev.classmethod.jp/articles/20261120-amazon-s3-tables-replication-writable-tables/)

## 概要

Amazon S3 Tables の読み取り専用レプリカを書き込み可能なテーブルに昇格できるようになりました。namespace とテーブル名は変わらず、リージョン障害時に書き込み先を切り替えられます。東京から大阪で、コンソールからの切り離しと Athena での書き込みを試しました。

---

*この記事は自動収集システムによって保存されました。*
