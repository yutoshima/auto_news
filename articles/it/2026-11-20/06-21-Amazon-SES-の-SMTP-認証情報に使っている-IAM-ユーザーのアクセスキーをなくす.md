---
title: "Amazon SES の SMTP 認証情報に使っている IAM ユーザーのアクセスキーをなくす"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T06:21:16
url: https://dev.classmethod.jp/articles/ses-smtp-credentials-without-access-keys/
---

# Amazon SES の SMTP 認証情報に使っている IAM ユーザーのアクセスキーをなくす

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 06:21
- **URL**: [https://dev.classmethod.jp/articles/ses-smtp-credentials-without-access-keys/](https://dev.classmethod.jp/articles/ses-smtp-credentials-without-access-keys/)

## 概要

Amazon SES の SMTP 認証情報の実体は IAM ユーザーのアクセスキーです。送信を SES API と IAM ロールに変える方法と、SMTP しか話せないアプリケーションを Mail Manager に切り替える方法のいずれかで、アクセスキーをなくす手順を紹介します。

---

*この記事は自動収集システムによって保存されました。*
