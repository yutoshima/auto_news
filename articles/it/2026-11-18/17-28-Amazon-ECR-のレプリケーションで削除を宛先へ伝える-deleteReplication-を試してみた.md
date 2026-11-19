---
title: "Amazon ECR のレプリケーションで削除を宛先へ伝える deleteReplication を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-18T17:28:52
url: https://dev.classmethod.jp/articles/amazon-ecr-replication-delete-replication/
---

# Amazon ECR のレプリケーションで削除を宛先へ伝える deleteReplication を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月18日 17:28
- **URL**: [https://dev.classmethod.jp/articles/amazon-ecr-replication-delete-replication/](https://dev.classmethod.jp/articles/amazon-ecr-replication-delete-replication/)

## 概要

Amazon ECR のレプリケーションで deleteReplication を有効化すると、有効化後にソースで行ったイメージやタグの削除が宛先にも反映されます。us-east-1 から us-east-2 へのレプリケーションで試すと、タグ指定とダイジェスト指定の削除は数秒で反映され、宛先の CloudTrail に記録されました。

---

*この記事は自動収集システムによって保存されました。*
