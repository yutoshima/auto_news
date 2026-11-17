---
title: "[Grafana] Ductus で、直近 7 日は DynamoDB、それより前は S3 + Athena から読んで、Grafana の 1 本の線にしてみました"
source: "DevelopersIO"
category: "it"
published: 2026-11-16T15:09:37
url: https://dev.classmethod.jp/articles/dynamodb-ductus-hot-cold-athena-grafana/
---

# [Grafana] Ductus で、直近 7 日は DynamoDB、それより前は S3 + Athena から読んで、Grafana の 1 本の線にしてみました

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月16日 15:09
- **URL**: [https://dev.classmethod.jp/articles/dynamodb-ductus-hot-cold-athena-grafana/](https://dev.classmethod.jp/articles/dynamodb-ductus-hot-cold-athena-grafana/)

## 概要

DynamoDB と S3 に分けたセンサーデータを、Grafana で 1 本の線として表示するため、Ductus のコールドストア機能を使用した例を紹介させていただきました。

---

*この記事は自動収集システムによって保存されました。*
