---
title: "Amazon Bedrock AgentCore Gatewayのレート制限をユーザーごとにかけられるか検証してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-24T00:00:12
url: https://dev.classmethod.jp/articles/agentcore-gateway-rate-limit-per-user/
---

# Amazon Bedrock AgentCore Gatewayのレート制限をユーザーごとにかけられるか検証してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月24日 00:00
- **URL**: [https://dev.classmethod.jp/articles/agentcore-gateway-rate-limit-per-user/](https://dev.classmethod.jp/articles/agentcore-gateway-rate-limit-per-user/)

## 概要

Amazon Bedrock AgentCore Gatewayのレート制限で、JWTのusernameクレームごとにリクエスト数の上限を分けられるかを検証しました。上限を超えた呼び出しが止まるか、1人の使いすぎが他のユーザーに影響しないかなど、5つの点を確認したので紹介します。

---

*この記事は自動収集システムによって保存されました。*
