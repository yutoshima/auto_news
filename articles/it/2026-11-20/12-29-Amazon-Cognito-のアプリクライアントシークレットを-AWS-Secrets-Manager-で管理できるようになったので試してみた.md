---
title: "Amazon Cognito のアプリクライアントシークレットを AWS Secrets Manager で管理できるようになったので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T12:29:10
url: https://dev.classmethod.jp/articles/cognito-app-client-secret-secrets-manager/
---

# Amazon Cognito のアプリクライアントシークレットを AWS Secrets Manager で管理できるようになったので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 12:29
- **URL**: [https://dev.classmethod.jp/articles/cognito-app-client-secret-secrets-manager/](https://dev.classmethod.jp/articles/cognito-app-client-secret-secrets-manager/)

## 概要

Amazon Cognito のアプリクライアントシークレットを AWS Secrets Manager で管理できるようになりました。新規のアプリクライアントで有効化すると応答に ClientSecretArn が返ること、Secrets Manager から取得した値で認証できることを AWS CLI で確認しました。

---

*この記事は自動収集システムによって保存されました。*
