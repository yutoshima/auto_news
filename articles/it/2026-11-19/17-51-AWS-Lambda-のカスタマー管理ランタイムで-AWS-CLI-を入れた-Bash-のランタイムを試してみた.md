---
title: "AWS Lambda のカスタマー管理ランタイムで AWS CLI を入れた Bash のランタイムを試してみた\""
source: "DevelopersIO"
category: "it"
published: 2026-11-19T17:51:32
url: https://dev.classmethod.jp/articles/lambda-customer-managed-runtimes-bash-runtime/
---

# AWS Lambda のカスタマー管理ランタイムで AWS CLI を入れた Bash のランタイムを試してみた"

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 17:51
- **URL**: [https://dev.classmethod.jp/articles/lambda-customer-managed-runtimes-bash-runtime/](https://dev.classmethod.jp/articles/lambda-customer-managed-runtimes-bash-runtime/)

## 概要

Docker イメージのビルドと ECR への push、`aws lambda-core` での runtime・version・alias の作成までの手順を紹介します。この runtime を使い、ZIP 圧縮したシェルスクリプトで Lambda 関数を作成すると、関数内で AWS CLI を実行できました。

---

*この記事は自動収集システムによって保存されました。*
