---
title: "GrafanaのアラートからDevOps Agentの調査を自動で起動して、結果をSlackに通知してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-29T07:01:52
url: https://dev.classmethod.jp/articles/devops-agent-grafana-alert-webhook-slack/
---

# GrafanaのアラートからDevOps Agentの調査を自動で起動して、結果をSlackに通知してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月29日 07:01
- **URL**: [https://dev.classmethod.jp/articles/devops-agent-grafana-alert-webhook-slack/](https://dev.classmethod.jp/articles/devops-agent-grafana-alert-webhook-slack/)

## 概要

ECS FargateでセルフホストしたGrafanaのアラートから、公式の通知テンプレートでAWS DevOps Agentの調査を自動で起動し、結果をSlackに通知してみました。アラートの`summary`の書き方による調査の違いや、アラートが再発火したときの挙動も確認しました。

---

*この記事は自動収集システムによって保存されました。*
