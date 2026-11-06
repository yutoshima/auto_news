---
title: "Lambda Web Functions のキャッシュを ElastiCache Serverless for Valkey に置いてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-05T04:42:18
url: https://dev.classmethod.jp/articles/lambda-web-functions-valkey-serverless-cda-cache/
---

# Lambda Web Functions のキャッシュを ElastiCache Serverless for Valkey に置いてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 04:42
- **URL**: [https://dev.classmethod.jp/articles/lambda-web-functions-valkey-serverless-cda-cache/](https://dev.classmethod.jp/articles/lambda-web-functions-valkey-serverless-cda-cache/)

## 概要

DevelopersIO を ECS から Lambda Web Functions へ移した際、Next.js のメモリとファイルに置いていた Contentful CDA のキャッシュを ElastiCache Serverless for Valkey に置き換えました。構成と実測値を紹介します。

---

*この記事は自動収集システムによって保存されました。*
