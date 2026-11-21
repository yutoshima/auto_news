---
title: "AWS STS の GetScopedCredentials で一時認証情報の権限とセッション期間を絞ってみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T14:08:06
url: https://dev.classmethod.jp/articles/aws-sts-getscopedcredentials-scope-down/
---

# AWS STS の GetScopedCredentials で一時認証情報の権限とセッション期間を絞ってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 14:08
- **URL**: [https://dev.classmethod.jp/articles/aws-sts-getscopedcredentials-scope-down/](https://dev.classmethod.jp/articles/aws-sts-getscopedcredentials-scope-down/)

## 概要

AWS STS の GetScopedCredentials で、既存の一時認証情報から権限とセッション期間を絞った認証情報を発行しました。発行した認証情報の ARN は呼び出し元と同じで、権限と期間は呼び出し元の範囲に収まりました。発行の呼び出しは CloudTrail に記録されました。

---

*この記事は自動収集システムによって保存されました。*
