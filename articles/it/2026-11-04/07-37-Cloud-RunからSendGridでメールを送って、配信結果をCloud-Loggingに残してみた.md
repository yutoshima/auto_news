---
title: "Cloud RunからSendGridでメールを送って、配信結果をCloud Loggingに残してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-04T07:37:15
url: https://dev.classmethod.jp/articles/cloud-run-sendgrid-event-webhook-cloud-logging/
---

# Cloud RunからSendGridでメールを送って、配信結果をCloud Loggingに残してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月04日 07:37
- **URL**: [https://dev.classmethod.jp/articles/cloud-run-sendgrid-event-webhook-cloud-logging/](https://dev.classmethod.jp/articles/cloud-run-sendgrid-event-webhook-cloud-logging/)

## 概要

Google CloudにはSESに当たるサービスがないため、Cloud RunからSendGridのWeb APIでメールを送り、配信や開封の結果をEvent WebhookでCloud Loggingに残してみました。受信側では署名を検証し、SendGrid以外からのリクエストを拒否しています。

---

*この記事は自動収集システムによって保存されました。*
