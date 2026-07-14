---
title: "AWS Elastic Disaster Recoveryが、Amazon EBS ボリュームの初期化レートをサポートしました"
source: "AWS What's New"
category: "it"
published: 2026-07-14T22:00:56
url: https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/
---

# AWS Elastic Disaster Recoveryが、Amazon EBS ボリュームの初期化レートをサポートしました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年07月14日 22:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/)

## 概要

AWS Elastic Disaster Recovery（AWS DRS）は現在、Amazon EBSボリュームの初期化レートをサポートしています。これにより、 drill（訓練）や復旧時に回復済みボリュームが完全な性能に早く達するのを助けます。DRSがスナップショからEBSボリュームを復元する場合、データは背景でAmazon S3から読み込まれ、まだ読み込まれていないブロックへのI/Oは初期化が完了するまで遅くなることがあります。このリリースにより、DRSが管理するEC2起動テンプレートにボリューム初期化レートを設定でき、DRSが自動的に適用します。

---

*この記事は自動収集システムによって保存されました。*
