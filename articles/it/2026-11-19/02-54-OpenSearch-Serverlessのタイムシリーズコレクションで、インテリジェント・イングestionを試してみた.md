---
title: "OpenSearch Serverlessのタイムシリーズコレクションで、インテリジェント・イングestionを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T02:54:10
url: https://dev.classmethod.jp/articles/amazon-opensearch-serverless-time-series-intelligent-ingestion/
---

# OpenSearch Serverlessのタイムシリーズコレクションで、インテリジェント・イングestionを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 02:54
- **URL**: [https://dev.classmethod.jp/articles/amazon-opensearch-serverless-time-series-intelligent-ingestion/](https://dev.classmethod.jp/articles/amazon-opensearch-serverless-time-series-intelligent-ingestion/)

## 概要

S3 に置いた NDJSON と JSON array のログを、ingestion job で取り込みました。NDJSON では、@timestamp が不正なドキュメントは専用のインデックスに残り、欠落したドキュメントは拒否されず S3 の更新日時が入りました。

---

*この記事は自動収集システムによって保存されました。*
