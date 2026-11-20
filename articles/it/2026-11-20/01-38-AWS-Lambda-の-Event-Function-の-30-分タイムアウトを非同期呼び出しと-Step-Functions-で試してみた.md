---
title: "AWS Lambda の Event Function の 30 分タイムアウトを非同期呼び出しと Step Functions で試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T01:38:31
url: https://dev.classmethod.jp/articles/aws-lambda-event-function-30-minute-timeout/
---

# AWS Lambda の Event Function の 30 分タイムアウトを非同期呼び出しと Step Functions で試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 01:38
- **URL**: [https://dev.classmethod.jp/articles/aws-lambda-event-function-30-minute-timeout/](https://dev.classmethod.jp/articles/aws-lambda-event-function-30-minute-timeout/)

## 概要

AWS Lambda の on-demand Event Function に 1,800 秒のタイムアウトを設定し、非同期呼び出しと Step Functions Standard で実行しました。どちらも 15 分を超えて動作、1,800 秒まで動き続ける関数は 1,800 秒で打ち切られました。

---

*この記事は自動収集システムによって保存されました。*
