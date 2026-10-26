---
title: "[DynamoDB] ネイティブベクトル検索で、外観検査の良品記録を業務データごと引いて、未知の不良を見つけてみました"
source: "DevelopersIO"
category: "it"
published: 2026-10-26T00:15:25
url: https://dev.classmethod.jp/articles/dynamodb-vector-search-defect-inspection/
---

# [DynamoDB] ネイティブベクトル検索で、外観検査の良品記録を業務データごと引いて、未知の不良を見つけてみました

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 00:15
- **URL**: [https://dev.classmethod.jp/articles/dynamodb-vector-search-defect-inspection/](https://dev.classmethod.jp/articles/dynamodb-vector-search-defect-inspection/)

## 概要

Amazon DynamoDBのネイティブベクトル検索機能を使い、外観検査で未知の不良を検出する仕組みを実装してみました。ベクトルと検査記録を同じアイテムに置くことで、異常スコアと根拠となった良品記録を1回の検索で返せます。

---

*この記事は自動収集システムによって保存されました。*
