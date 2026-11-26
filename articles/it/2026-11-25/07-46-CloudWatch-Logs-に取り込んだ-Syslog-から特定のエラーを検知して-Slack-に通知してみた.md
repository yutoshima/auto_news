---
title: "CloudWatch Logs に取り込んだ Syslog から特定のエラーを検知して Slack に通知してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-25T07:46:08
url: https://dev.classmethod.jp/articles/cloudwatch-logs-managed-syslog-error-detection-slack-notification/
---

# CloudWatch Logs に取り込んだ Syslog から特定のエラーを検知して Slack に通知してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 07:46
- **URL**: [https://dev.classmethod.jp/articles/cloudwatch-logs-managed-syslog-error-detection-slack-notification/](https://dev.classmethod.jp/articles/cloudwatch-logs-managed-syslog-error-detection-slack-notification/)

## 概要

CloudWatch Logs のマネージド Syslog 取り込みで収集したログから特定のエラーを検知し、重複通知を抑えながら Slack へ自動通知する仕組みを構築しました。Lambda、EventBridge Scheduler、SSM Parameter Store を組み合わせて、実装と検証を行った結果をまとめます。

---

*この記事は自動収集システムによって保存されました。*
