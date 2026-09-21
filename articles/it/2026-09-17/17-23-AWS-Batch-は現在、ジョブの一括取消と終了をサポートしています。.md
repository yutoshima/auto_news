---
title: "AWS Batch は現在、ジョブの一括取消と終了をサポートしています。"
source: "AWS What's New"
category: "it"
published: 2026-09-17T17:23:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/
---

# AWS Batch は現在、ジョブの一括取消と終了をサポートしています。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月17日 17:23
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/)

## 概要

AWS Batch は一括のジョブキャンセルと終了をサポートするようになり、1 回の API 呼び出しで最大 50 件のジョブをキャンセルまたは終了できるようになりました。新しい CancelJobs、TerminateJobs、TerminateServiceJobs API により、大規模なバッチワークロードの運用負荷が低減され、複数のジョブグループに一度に対処し、単一の応答で各ジョブの結果を受け取ることができます。さらに、ListJobs は now が isCancelled および isTerminated フィールドを返すようになり、ListServiceJobs は isTerminated を返すようになり、より簡便になります。

---

*この記事は自動収集システムによって保存されました。*
