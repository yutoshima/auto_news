---
title: "DevOps Agent の スキルとカスタムエージェントを使って、GuardDuty 検出結果を重要度別に振り分けて Slack 通知してみる"
source: "DevelopersIO"
category: "it"
published: 2026-11-05T08:54:40
url: https://dev.classmethod.jp/articles/devops-agent-triage-and-notify-slack/
---

# DevOps Agent の スキルとカスタムエージェントを使って、GuardDuty 検出結果を重要度別に振り分けて Slack 通知してみる

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 08:54
- **URL**: [https://dev.classmethod.jp/articles/devops-agent-triage-and-notify-slack/](https://dev.classmethod.jp/articles/devops-agent-triage-and-notify-slack/)

## 概要

GuardDuty の検出を重要度別に振り分け、DevOps Agent 連携を検証してみました。LOW はログ記録のみ、MEDIUM はカスタムエージェント、HIGH は本調査、という3段階の運用フローを実装し、実際の動作確認を交えて紹介します。

---

*この記事は自動収集システムによって保存されました。*
