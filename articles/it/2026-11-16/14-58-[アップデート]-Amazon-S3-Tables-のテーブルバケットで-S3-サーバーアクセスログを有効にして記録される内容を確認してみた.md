---
title: "[アップデート] Amazon S3 Tables のテーブルバケットで S3 サーバーアクセスログを有効にして記録される内容を確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-16T14:58:51
url: https://dev.classmethod.jp/articles/20261116-amazon-s3-tables-server-logs/
---

# [アップデート] Amazon S3 Tables のテーブルバケットで S3 サーバーアクセスログを有効にして記録される内容を確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月16日 14:58
- **URL**: [https://dev.classmethod.jp/articles/20261116-amazon-s3-tables-server-logs/](https://dev.classmethod.jp/articles/20261116-amazon-s3-tables-server-logs/)

## 概要

Amazon S3 Tables のテーブルバケットが S3 サーバーアクセスログに対応し、テーブル操作とデータの読み書きを追加料金なしで記録できるようになりました。AWS CLI で設定し、Athena でクエリ ID ごとの読み書きを集計した結果と、設定するロールに必要な S3 権限を紹介します。

---

*この記事は自動収集システムによって保存されました。*
