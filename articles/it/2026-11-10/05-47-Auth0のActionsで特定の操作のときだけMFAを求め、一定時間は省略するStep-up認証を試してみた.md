---
title: "Auth0のActionsで特定の操作のときだけMFAを求め、一定時間は省略するStep-up認証を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-10T05:47:02
url: https://dev.classmethod.jp/articles/auth0-step-up-mfa/
---

# Auth0のActionsで特定の操作のときだけMFAを求め、一定時間は省略するStep-up認証を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 05:47
- **URL**: [https://dev.classmethod.jp/articles/auth0-step-up-mfa/](https://dev.classmethod.jp/articles/auth0-step-up-mfa/)

## 概要

Auth0のActionsを使って、ユーザー情報変更などの重要な操作のときだけMFAを求め、一度通したら一定時間は省略するStep-up認証を実装してみました。実装のポイントと、アプリケーション側で気を付けるべき判定方法をご紹介します。

---

*この記事は自動収集システムによって保存されました。*
