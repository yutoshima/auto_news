---
title: "Amazon RDS がコンソールと API にスナップショットのサイズ情報を完全に追加しました"
source: "AWS What's New"
category: "it"
published: 2026-09-29T21:00:23
url: https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-full-snapshot-size-available/
---

# Amazon RDS がコンソールと API にスナップショットのサイズ情報を完全に追加しました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月29日 21:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-full-snapshot-size-available/](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-full-snapshot-size-available/)

## 概要

Amazon RDS は現在、RDS スナップショットの全スナップショイトサイズを表示します。この改善により、顧客は新しいフィールド「FullSnapshotSizeInBytes」を使用して DescribeDBSnapshots API からプログラム的に全スナップショイトサイズを取得できるようになりました。また、コンソールの「Full Snapshot Size」列でもこの情報を閲覧できます。

Amazon RDS のスナップショットは増分です。つまり、時系列でボリュームの複数のスナップショットを作成すると、各スナップショットは新規または変更されたブロックのみを保存します。

---

*この記事は自動収集システムによって保存されました。*
