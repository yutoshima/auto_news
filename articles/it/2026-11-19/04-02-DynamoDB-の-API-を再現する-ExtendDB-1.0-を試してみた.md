---
title: "DynamoDB の API を再現する ExtendDB 1.0 を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T04:02:38
url: https://dev.classmethod.jp/articles/aws-extenddb-1-0-dev-image-npm/
---

# DynamoDB の API を再現する ExtendDB 1.0 を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 04:02
- **URL**: [https://dev.classmethod.jp/articles/aws-extenddb-1-0-dev-image-npm/](https://dev.classmethod.jp/articles/aws-extenddb-1-0-dev-image-npm/)

## 概要

AWS が公開した DynamoDB 互換アダプタ ExtendDB 1.0 を、dev イメージ、@extenddb/dev、PostgreSQL 構成で動かし、同じ操作を実際の DynamoDB にも流して応答を比べました。AWS CLI と SDK の基本操作は通り、違いは、テーブル作成直後の状態やエラーの扱いなどに見られました。

---

*この記事は自動収集システムによって保存されました。*
