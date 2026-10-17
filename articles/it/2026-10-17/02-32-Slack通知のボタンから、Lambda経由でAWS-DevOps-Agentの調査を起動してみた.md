---
title: "Slack通知のボタンから、Lambda経由でAWS DevOps Agentの調査を起動してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-17T02:32:12
url: https://dev.classmethod.jp/articles/hasuto-devops-agent-slack-button-lambda/
---

# Slack通知のボタンから、Lambda経由でAWS DevOps Agentの調査を起動してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 02:32
- **URL**: [https://dev.classmethod.jp/articles/hasuto-devops-agent-slack-button-lambda/](https://dev.classmethod.jp/articles/hasuto-devops-agent-slack-button-lambda/)

## 概要

Slackのアラーム通知にAmazon Qのカスタムアクションでボタンを付け、押したときだけLambda経由でAWS DevOps Agentの調査を起動する構成を作りました。ボタンはチャンネルロールの権限で動き、表示条件は起動の制限にならないため、許可リストと状態の確認をLambdaに置いています。

---

*この記事は自動収集システムによって保存されました。*
