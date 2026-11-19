---
title: "Cognito ID プールのプリンシパルタグで、既存ユーザーIDを引き継いだまま DynamoDB の行レベル制御をしてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-18T08:21:10
url: https://dev.classmethod.jp/articles/cognito-abac-dynamodb-legacy-user-id/
---

# Cognito ID プールのプリンシパルタグで、既存ユーザーIDを引き継いだまま DynamoDB の行レベル制御をしてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月18日 08:21
- **URL**: [https://dev.classmethod.jp/articles/cognito-abac-dynamodb-legacy-user-id/](https://dev.classmethod.jp/articles/cognito-abac-dynamodb-legacy-user-id/)

## 概要

Cognito の ID プールで既存ユーザーIDと新規ユーザーの `sub` を混在させながら、DynamoDB の行レベルアクセス制御を実現する2つの方式を検証してみました。カスタム属性とLambda トリガーの使い分けについて紹介します。

---

*この記事は自動収集システムによって保存されました。*
