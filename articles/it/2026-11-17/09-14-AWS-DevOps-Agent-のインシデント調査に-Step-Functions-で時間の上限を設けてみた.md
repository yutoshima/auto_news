---
title: "AWS DevOps Agent のインシデント調査に Step Functions で時間の上限を設けてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-17T09:14:35
url: https://dev.classmethod.jp/articles/aws-devops-agent-investigation-timeout-step-functions/
---

# AWS DevOps Agent のインシデント調査に Step Functions で時間の上限を設けてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月17日 09:14
- **URL**: [https://dev.classmethod.jp/articles/aws-devops-agent-investigation-timeout-step-functions/](https://dev.classmethod.jp/articles/aws-devops-agent-investigation-timeout-step-functions/)

## 概要

Step Functions から調査を開始し、上限時間を過ぎても終わっていない調査を、AWS SDK 統合の UpdateBacklogTask で取り消す仕組みを作りました。

---

*この記事は自動収集システムによって保存されました。*
