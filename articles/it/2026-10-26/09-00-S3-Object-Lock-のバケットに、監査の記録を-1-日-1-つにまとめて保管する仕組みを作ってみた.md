---
title: "S3 Object Lock のバケットに、監査の記録を 1 日 1 つにまとめて保管する仕組みを作ってみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-26T09:00:10
url: https://dev.classmethod.jp/articles/s3-object-lock-eventbridge-scheduler-daily-archive/
---

# S3 Object Lock のバケットに、監査の記録を 1 日 1 つにまとめて保管する仕組みを作ってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 09:00
- **URL**: [https://dev.classmethod.jp/articles/s3-object-lock-eventbridge-scheduler-daily-archive/](https://dev.classmethod.jp/articles/s3-object-lock-eventbridge-scheduler-daily-archive/)

## 概要

Amazon S3 Object Lock と条件付き書き込みを使い、監査ログの重複保管を防ぐ仕組みを実装しました。EventBridge Scheduler で毎日実行される Lambda 関数が同じ日分を複数回書き込もうとしても、条件付き書き込みによって 2 回目以降は自動的に拒否され、バケット内には 1 つのバージョンだけが残ります。その仕組みと検証結果を紹介します。

---

*この記事は自動収集システムによって保存されました。*
