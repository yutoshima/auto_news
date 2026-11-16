---
title: "[新機能] Snowflake の Temporary role grants がプレビューとなったので、ロールを期限付きでユーザーに付与し 4 つのユースケースで失効時の挙動を確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-15T14:35:41
url: https://dev.classmethod.jp/articles/snowflake-temporary-role-grants-preview/
---

# [新機能] Snowflake の Temporary role grants がプレビューとなったので、ロールを期限付きでユーザーに付与し 4 つのユースケースで失効時の挙動を確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 14:35
- **URL**: [https://dev.classmethod.jp/articles/snowflake-temporary-role-grants-preview/](https://dev.classmethod.jp/articles/snowflake-temporary-role-grants-preview/)

## 概要

Snowflakeで期限付きロール付与が可能になった「Temporary role grants」を試してみました。オンコール対応、PII一時閲覧、期間限定メンバー、管理者権限の4つのユースケースから、失効時の動作や再付与時の挙動まで、実装時に知っておきたい仕様を検証します。

---

*この記事は自動収集システムによって保存されました。*
