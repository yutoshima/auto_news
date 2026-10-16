---
title: "Amazon DynamoDB Streamsは、タイムスタンプベースのストリーム処理をサポートします。"
source: "AWS What's New"
category: "it"
published: 2026-10-15T18:30:00
url: https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-dynamodb-streams-timestamp-processing
---

# Amazon DynamoDB Streamsは、タイムスタンプベースのストリーム処理をサポートします。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 18:30
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-dynamodb-streams-timestamp-processing](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-dynamodb-streams-timestamp-processing)

## 概要

<p>Amazon DynamoDB Streams は現在、タイムスタンプベースのストリーム処理をサポートしており、特定の時点からストリームレコードの読み取りを開始できます。以前は、保持されている最も古いレコード（最大24時間前）から開始するか、ストリームの読み取りを開始した後に書き込まれた新しいレコードから開始するしかありませんでした。 now, you can supply a timestamp and begin processing at the first record written at or after that time using the AT_TIMESTAMP shard iterator type.</p>

日本語訳:

---

*この記事は自動収集システムによって保存されました。*
