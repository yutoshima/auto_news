---
title: "Amazon Cognito のマルチリージョンレプリケーションで、東京のユーザープールのレプリカを大阪に作ってみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-23T16:45:35
url: https://dev.classmethod.jp/articles/amazon-cognito-mrr-osaka-replica/
---

# Amazon Cognito のマルチリージョンレプリケーションで、東京のユーザープールのレプリカを大阪に作ってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 16:45
- **URL**: [https://dev.classmethod.jp/articles/amazon-cognito-mrr-osaka-replica/](https://dev.classmethod.jp/articles/amazon-cognito-mrr-osaka-replica/)

## 概要

Amazon Cognito のマルチリージョンレプリケーション（MRR）の追加リージョン対応を受け、東京のユーザープールのレプリカを大阪に作成しました。INACTIVE のレプリカでも東京で作成したユーザーを大阪から読み取れ、ACTIVE にすると大阪のエンドポイントでトークンを取得できました。

---

*この記事は自動収集システムによって保存されました。*
