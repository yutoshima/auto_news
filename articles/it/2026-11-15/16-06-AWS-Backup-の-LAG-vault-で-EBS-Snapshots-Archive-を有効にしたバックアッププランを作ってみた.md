---
title: "AWS Backup の LAG vault で EBS Snapshots Archive を有効にしたバックアッププランを作ってみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-15T16:06:40
url: https://dev.classmethod.jp/articles/aws-backup-lag-vault-ebs-archive/
---

# AWS Backup の LAG vault で EBS Snapshots Archive を有効にしたバックアッププランを作ってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 16:06
- **URL**: [https://dev.classmethod.jp/articles/aws-backup-lag-vault-ebs-archive/](https://dev.classmethod.jp/articles/aws-backup-lag-vault-ebs-archive/)

## 概要

LAG vault 内の EBS バックアップをアーカイブへ移すためのプラン作成を試しました。プランの条件は、頻度が月に 1 回以下で、総保持期間が warm の期間より 90 日以上長いことでした。

---

*この記事は自動収集システムによって保存されました。*
