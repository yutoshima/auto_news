---
title: "Amazon ECR の replication backfill で既存イメージを別リージョンへ複製してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-28T05:50:38
url: https://dev.classmethod.jp/articles/ecr-replication-backfill-existing-images/
---

# Amazon ECR の replication backfill で既存イメージを別リージョンへ複製してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 05:50
- **URL**: [https://dev.classmethod.jp/articles/ecr-replication-backfill-existing-images/](https://dev.classmethod.jp/articles/ecr-replication-backfill-existing-images/)

## 概要

Amazon ECR の replication backfill で、レプリケーションの設定前に push した既存イメージを東京からバージニア北部へ複製しました。backfill を実行すると、送信元と同じダイジェストのイメージが送信先に揃いました。

---

*この記事は自動収集システムによって保存されました。*
