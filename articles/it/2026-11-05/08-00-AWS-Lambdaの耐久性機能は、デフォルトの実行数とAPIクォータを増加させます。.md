---
title: "AWS Lambdaの耐久性機能は、デフォルトの実行数とAPIクォータを増加させます。"
source: "AWS What's New"
category: "it"
published: 2026-11-05T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-functions-default-quotas/
---

# AWS Lambdaの耐久性機能は、デフォルトの実行数とAPIクォータを増加させます。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-functions-default-quotas/](https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-functions-default-quotas/)

## 概要

AWS Lambda の durable functions の実行上限が引き上げられました。以下の新しいクォータは、US East（N. Virginia）、US West（Oregon）、Europe（Ireland）を除くすべてのAWSリージョンで適用されます。これらのリージョンでは上限が倍になります。

- 1アカウントあたりのdurable executionsの実行数（100万 → 500万）
- durable executionsを開始するための関数呼び出しレート（1秒あたり300 → 3,000リクエスト）
- CheckpointDurableExecution および GetDurableExecutionState

---

*この記事は自動収集システムによって保存されました。*
