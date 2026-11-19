---
title: "Amazon Cognito の CloudTrail イベントで HIDDEN_DUE_TO_SECURITY_REASONS となっているユーザーを sub から特定してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-18T09:18:38
url: https://dev.classmethod.jp/articles/cognito-cloudtrail-identify-user-by-sub/
---

# Amazon Cognito の CloudTrail イベントで HIDDEN_DUE_TO_SECURITY_REASONS となっているユーザーを sub から特定してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月18日 09:18
- **URL**: [https://dev.classmethod.jp/articles/cognito-cloudtrail-identify-user-by-sub/](https://dev.classmethod.jp/articles/cognito-cloudtrail-identify-user-by-sub/)

## 概要

Amazon Cognito の管理 API の CloudTrail イベントで、username が HIDDEN_DUE_TO_SECURITY_REASONS になっていた場合、additionalEventData の sub から ListUsers で対象のユーザーを特定してみました。

---

*この記事は自動収集システムによって保存されました。*
