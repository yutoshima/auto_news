---
title: "AWS Lambda の関数状態変化イベントを EventBridge ルールで受け取ってみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-22T13:54:46
url: https://dev.classmethod.jp/articles/aws-lambda-function-state-events-eventbridge/
---

# AWS Lambda の関数状態変化イベントを EventBridge ルールで受け取ってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月22日 13:54
- **URL**: [https://dev.classmethod.jp/articles/aws-lambda-function-state-events-eventbridge/](https://dev.classmethod.jp/articles/aws-lambda-function-state-events-eventbridge/)

## 概要

Lambda 関数のデプロイや状態の変化を、GetFunction API のポーリングなしで EventBridge のイベントとして拾えるようになりました。関数の作成・更新・公開・削除で実際に届くイベントの種類と中身を確認し、関数 ARN と state で絞り込むルールも試しました。

---

*この記事は自動収集システムによって保存されました。*
