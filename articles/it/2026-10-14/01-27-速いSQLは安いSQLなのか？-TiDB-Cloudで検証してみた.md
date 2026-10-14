---
title: "速いSQLは安いSQLなのか？ TiDB Cloudで検証してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-14T01:27:06
url: https://dev.classmethod.jp/articles/tidb-cloud-starter-sql-latency-vs-ru/
---

# 速いSQLは安いSQLなのか？ TiDB Cloudで検証してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 01:27
- **URL**: [https://dev.classmethod.jp/articles/tidb-cloud-starter-sql-latency-vs-ru/](https://dev.classmethod.jp/articles/tidb-cloud-starter-sql-latency-vs-ru/)

## 概要

TiDB Cloud Starter で、3 種類の方法で速くした SQL の実行時間と RU を計測しました。実行時間とともに RU も大きく削減できたのは SQL が読むデータを減らした場合だけで、並列度を上げて速くした場合の RU は変わらず、ロック待ちをなくした場合の RU の削減は実行時間の削減より小さくなりました。

---

*この記事は自動収集システムによって保存されました。*
