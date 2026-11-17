---
title: "EventBridge Schedulerが失敗したとき、どのエラーなら再試行されるのか？Lambda例外・権限なし・スロットリングで確かめてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-16T09:23:05
url: https://dev.classmethod.jp/articles/202611-mitsuguchi-eventbridge-scheduler-lambda-sqs-kensho/
---

# EventBridge Schedulerが失敗したとき、どのエラーなら再試行されるのか？Lambda例外・権限なし・スロットリングで確かめてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月16日 09:23
- **URL**: [https://dev.classmethod.jp/articles/202611-mitsuguchi-eventbridge-scheduler-lambda-sqs-kensho/](https://dev.classmethod.jp/articles/202611-mitsuguchi-eventbridge-scheduler-lambda-sqs-kensho/)

## 概要

EventBridge Schedulerが失敗したとき、本当に再試行されるのか。Lambda例外・権限エラー・スロットリング・フレキシブルタイムウィンドウなど、複数のケースを実際に試して、再試行とDLQの動きを確かめてみました。

---

*この記事は自動収集システムによって保存されました。*
