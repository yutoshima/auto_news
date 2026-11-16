---
title: "CognitoのOAuth 2.0トークン交換でMCP向けにスコープを絞る利用を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-15T09:15:05
url: https://dev.classmethod.jp/articles/cognito-oauth2-token-exchange-scoped-token/
---

# CognitoのOAuth 2.0トークン交換でMCP向けにスコープを絞る利用を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 09:15
- **URL**: [https://dev.classmethod.jp/articles/cognito-oauth2-token-exchange-scoped-token/](https://dev.classmethod.jp/articles/cognito-oauth2-token-exchange-scoped-token/)

## 概要

Amazon Cognito の OAuth 2.0 トークン交換（GetDerivedToken）で、MCP サーバー向けにスコープを絞ったトークンを発行しました。API Gateway と AgentCore Gateway で、絞ったトークンは必要なスコープが足りず拒否されることを確認できました。

---

*この記事は自動収集システムによって保存されました。*
