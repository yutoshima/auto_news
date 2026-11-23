---
title: "EventBridge の Webhook Events がサポートされたので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-22T15:36:03
url: https://dev.classmethod.jp/articles/eventbridge-webhook-events-sqs/
---

# EventBridge の Webhook Events がサポートされたので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月22日 15:36
- **URL**: [https://dev.classmethod.jp/articles/eventbridge-webhook-events-sqs/](https://dev.classmethod.jp/articles/eventbridge-webhook-events-sqs/)

## 概要

Amazon EventBridge の Webhook Events を試しました。HMAC 署名、静的トークン、Basic 認証の3方式で curl から送り、SQS 宛ての Subscriber で受け取りました。status での絞り込みと、署名違いの 403 拒否も確認しました。

---

*この記事は自動収集システムによって保存されました。*
