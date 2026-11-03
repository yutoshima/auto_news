---
title: "Amazon Kinesis Data Streams の拡張ファンアウトと共有スループットでレコードの遅延を比べてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-03T00:30:29
url: https://dev.classmethod.jp/articles/kinesis-enhanced-fan-out-vs-shared-throughput-latency/
---

# Amazon Kinesis Data Streams の拡張ファンアウトと共有スループットでレコードの遅延を比べてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 00:30
- **URL**: [https://dev.classmethod.jp/articles/kinesis-enhanced-fan-out-vs-shared-throughput-latency/](https://dev.classmethod.jp/articles/kinesis-enhanced-fan-out-vs-shared-throughput-latency/)

## 概要

Amazon Kinesis Data Streams のコンシューマーには共有スループットと拡張ファンアウトの 2 種類がありますが、実際の遅延はドキュメントの数字とどう違うのか。Lambda と boto3 の 4 通りのコンシューマーで、1 秒 5 件を 10 分送って測定してみました。

---

*この記事は自動収集システムによって保存されました。*
