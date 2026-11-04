---
title: "Amazon DynamoDB のテーブルをポイントインタイムリカバリで復元すると、TTL やストリームの設定が引き継がれません。設定し直す項目を教えてください"
source: "DevelopersIO"
category: "it"
published: 2026-11-03T08:00:16
url: https://dev.classmethod.jp/articles/tsnote-dynamodb-pitr-restore-settings-not-copied/
---

# Amazon DynamoDB のテーブルをポイントインタイムリカバリで復元すると、TTL やストリームの設定が引き継がれません。設定し直す項目を教えてください

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 08:00
- **URL**: [https://dev.classmethod.jp/articles/tsnote-dynamodb-pitr-restore-settings-not-copied/](https://dev.classmethod.jp/articles/tsnote-dynamodb-pitr-restore-settings-not-copied/)

## 概要

DynamoDB のポイントインタイムリカバリで復元したテーブルは、データとインデックスのみが引き継がれ、TTL・ストリーム・タグなどの設定は引き継がれません。復元後に自分で設定し直す必要がある項目と、その手順を実際の検証結果とともに紹介します。

---

*この記事は自動収集システムによって保存されました。*
