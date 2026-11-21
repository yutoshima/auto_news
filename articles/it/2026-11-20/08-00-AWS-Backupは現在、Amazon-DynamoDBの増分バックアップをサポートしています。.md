---
title: "AWS Backupは現在、Amazon DynamoDBの増分バックアップをサポートしています。"
source: "AWS What's New"
category: "it"
published: 2026-11-20T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-incremental-backups-dynamodb/
---

# AWS Backupは現在、Amazon DynamoDBの増分バックアップをサポートしています。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-incremental-backups-dynamodb/](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-incremental-backups-dynamodb/)

## 概要

AWS Backupは現在、Amazon DynamoDBテーブルのインクリメンタルバックアップをサポートしており、バックアップスケジュールを頻繁に設定したまま、バックアップストレージを削減できます。  
これまでは、AWS BackupはDynamoDBテーブルの完全なコピーを作成していました。今回のリリースにより、初回の完全バックアップ後は、各インクリメンタルバックアップが変更されたデータのみをキャプチャし、AWS Backupは15日ごとに新しい完全バックアップを取得します。これにより、データを少なく保ちながらより頻繁にバックアップを実行できます。任意の復元ポイントから復元できます。

---

*この記事は自動収集システムによって保存されました。*
