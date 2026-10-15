---
title: "AWS DevOps Agent、New Relic連携時の、Slack 通知について検証してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-14T07:24:50
url: https://dev.classmethod.jp/articles/devops-agent-newrelic-slack/
---

# AWS DevOps Agent、New Relic連携時の、Slack 通知について検証してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 07:24
- **URL**: [https://dev.classmethod.jp/articles/devops-agent-newrelic-slack/](https://dev.classmethod.jp/articles/devops-agent-newrelic-slack/)

## 概要

New Relic のアラートから AWS DevOps Agent に調査させ、結果を Slack に出す構成を実機で組みました。MCP なしだと DevOps Agent が New Relic のアラート情報を見られない問題と、その回避策、通知を1スレッドにまとめる方法を検証した結果をまとめます。

---

*この記事は自動収集システムによって保存されました。*
