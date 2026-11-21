---
title: "[アップデート] AWS STS の GetScopedCredentials で権限と有効期間を絞った認証情報を作ってみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T12:17:46
url: https://dev.classmethod.jp/articles/aws-sts-get-scoped-credentials/
---

# [アップデート] AWS STS の GetScopedCredentials で権限と有効期間を絞った認証情報を作ってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 12:17
- **URL**: [https://dev.classmethod.jp/articles/aws-sts-get-scoped-credentials/](https://dev.classmethod.jp/articles/aws-sts-get-scoped-credentials/)

## 概要

AWS STS に追加された GetScopedCredentials を AWS CLI から呼び出し、ID を変えずに権限と有効期間がどう絞られるのかを検証しました。また、絞り込みを重ねたときの上限や必要な許可も確かめてみました。

---

*この記事は自動収集システムによって保存されました。*
