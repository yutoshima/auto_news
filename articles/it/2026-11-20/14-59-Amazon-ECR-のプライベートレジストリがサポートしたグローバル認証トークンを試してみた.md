---
title: "Amazon ECR のプライベートレジストリがサポートしたグローバル認証トークンを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T14:59:32
url: https://dev.classmethod.jp/articles/aws-ecr-global-authentication-token/
---

# Amazon ECR のプライベートレジストリがサポートしたグローバル認証トークンを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 14:59
- **URL**: [https://dev.classmethod.jp/articles/aws-ecr-global-authentication-token/](https://dev.classmethod.jp/articles/aws-ecr-global-authentication-token/)

## 概要

us-east-1 で発行した1つのトークンで、ap-northeast-1 と eu-west-1 のプライベートレジストリに docker login、push、pull できました。トークンの発行手順と、複数リージョンでの使い方を紹介します。

---

*この記事は自動収集システムによって保存されました。*
