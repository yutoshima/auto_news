---
title: "Amazon S3 向け AWS Backup がバックアップデータへの直接アクセスをサポートしました"
source: "AWS What's New"
category: "it"
published: 2026-08-06T10:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/08/aws-backup-amazon-s3-direct-access/
---

# Amazon S3 向け AWS Backup がバックアップデータへの直接アクセスをサポートしました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年08月06日 10:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/08/aws-backup-amazon-s3-direct-access/](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-backup-amazon-s3-direct-access/)

## 概要

S3用のAWS Backupは、S3アクセスポイントの作成をサポートするようになりました。バックアップデータを復元を開始することなく、標準のS3 APIを使用して即座に読み取り専用アクセスを提供します。これにより、バックアップデータがバックアップボールト内で保護されたまま、ターゲットを絞ったファイルの復元、データ検証、コンプライアンス監査、鑑識調査を実施できます。

S3リカバリポイントのためにアクセスポイントを作成し、GetObject、HeadObject、ListObjectsV2 などの標準のS3操作を使用してバックアップデータを読み取ることができます。

---

*この記事は自動収集システムによって保存されました。*
