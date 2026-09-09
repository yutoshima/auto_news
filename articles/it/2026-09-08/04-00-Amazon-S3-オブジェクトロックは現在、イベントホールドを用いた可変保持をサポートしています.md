---
title: "Amazon S3 オブジェクトロックは現在、イベントホールドを用いた可変保持をサポートしています"
source: "AWS What's New"
category: "it"
published: 2026-09-08T04:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-object-lock-variable-retention/
---

# Amazon S3 オブジェクトロックは現在、イベントホールドを用いた可変保持をサポートしています

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月08日 04:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-object-lock-variable-retention/](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-object-lock-variable-retention/)

## 概要

<p>Amazon S3 Object Lockは現在、変動保持期間をサポートしています。これにより、契約の成立や監査の完了など、将来イベントを起点として必要保持期間が開始されるオブジェクトに対して、書き込みは1回・読み取りは複数回（WORM）保護を適用できます。オブジェクトにはイベントホールドと保持期間を設定し、ホールドが有効な間はS3がオブジェクトを保護します。ホールドを解除すると、S3は指定した期間、オブジェクトを保持します。法的開示保持（Legal holds）とは異なり、保護は即座に終了するわけではなく、設定した保持期間の終了時点で終了します。

---

*この記事は自動収集システムによって保存されました。*
