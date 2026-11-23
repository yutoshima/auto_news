---
title: "AWS BackupがAmazon DynamoDBの増分バックアップをサポートしました"
source: "AWS What's New"
category: "it"
published: 2026-11-20T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-incremental-backups-dynamodb/
---

# AWS BackupがAmazon DynamoDBの増分バックアップをサポートしました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-incremental-backups-dynamodb/](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-incremental-backups-dynamodb/)

## 概要

AWS Backupは現在、Amazon DynamoDBテーブルのインクリメンタルバックアップをサポートしており、バックアップを1時間単位での頻度を維持しつつ、バックアップストレージを削減できます。

これまでは、AWS BackupはDynamoDBテーブルの全コピーを作成していました。今回のリリースでは、初回のフルバックアップの後、各インクリメンタルバックアップは変更されたデータのみをキャプチャし、AWS Backupは15日ごとに新しいフルバックアップを作成します。これにより、データを少なく保存しつつ、より頻繁にバックアップを実行できます。任意の復元ポイントから復元できます。

---

*この記事は自動収集システムによって保存されました。*
