---
title: "AWS Batchは現在、ジョブの一括キャンセルと終了をサポートしています。"
source: "AWS What's New"
category: "it"
published: 2026-09-17T17:23:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/
---

# AWS Batchは現在、ジョブの一括キャンセルと終了をサポートしています。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月17日 17:23
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/)

## 概要

AWS Batchは現在、バルクジョブの取消と終了をサポートしており、1回のAPI呼び出しで最大50件のジョブを取消または終了できます。新しいCancelJobs、TerminateJobs、TerminateServiceJobs APIは、大規模なバッチ処理ワークロードの運用上の複雑さを軽減し、一度にグループ化されたジョブに対して操作を行い、単一の応答で各ジョブの結果を受け取ることができます。さらに、ListJobsはisCancelledおよびisTerminatedフィールドを返すようになり、ListServiceJobsはisTerminatedを返すようになるため、…

---

*この記事は自動収集システムによって保存されました。*
