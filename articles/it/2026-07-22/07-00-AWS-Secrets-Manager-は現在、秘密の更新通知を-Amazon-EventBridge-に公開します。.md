---
title: "AWS Secrets Manager は現在、秘密の更新通知を Amazon EventBridge に公開します。"
source: "AWS What's New"
category: "it"
published: 2026-07-22T07:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications
---

# AWS Secrets Manager は現在、秘密の更新通知を Amazon EventBridge に公開します。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年07月22日 07:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications](https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications)

## 概要

AWS Secrets Manager は、秘密の値が変更されるたびに自動的にイベントを Amazon EventBridge に公開するようになり、秘密の更新にリアルタイムで対応するイベント主導のワークフローを構築できるようになりました。  
これまでは、秘密の値が変更されたことを知るには、EventBridge に解析される AWS CloudTrail のイベントに依存する必要があり、ローテーションの成功、PutSecretValue、UpdateSecretValue など複数の API イベントを突き合わせる必要がありました。今回のリリースにより、Secrets Manager がイベントを直接公開します。

---

*この記事は自動収集システムによって保存されました。*
