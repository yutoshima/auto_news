---
title: "AWS Secrets Manager は、秘密の更新通知を Amazon EventBridge に配信するようになりました。"
source: "AWS What's New"
category: "it"
published: 2026-07-22T07:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications
---

# AWS Secrets Manager は、秘密の更新通知を Amazon EventBridge に配信するようになりました。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年07月22日 07:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications](https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications)

## 概要

AWS Secrets Manager が現在、秘密の値が変更されるたびに自動的に Amazon EventBridge にイベントを公開するようになり、秘密の更新にリアルタイムで対応できるイベント駆動型ワークフローを構築できるようになりました。  
従来は、秘密の値が変更されたことを知るために、EventBridge に解析された AWS CloudTrail のイベントを利用する必要があり、回転成功、PutSecretValue、UpdateSecretValue などの複数の API イベントを照合する必要がありました。今回のリリースにより、Secrets Manager がイベントを直接公開します。

---

*この記事は自動収集システムによって保存されました。*
