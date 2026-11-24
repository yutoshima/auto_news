---
title: "Amazon CloudWatch の PromQL でサポートされた 30 日幅のクエリを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-23T15:25:45
url: https://dev.classmethod.jp/articles/cloudwatch-promql-30day-query-window/
---

# Amazon CloudWatch の PromQL でサポートされた 30 日幅のクエリを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 15:25
- **URL**: [https://dev.classmethod.jp/articles/cloudwatch-promql-30day-query-window/](https://dev.classmethod.jp/articles/cloudwatch-promql-30day-query-window/)

## 概要

Amazon CloudWatch の PromQL で 30 日幅のクエリを試しました。query_range は 30 日分を 1 リクエストで取得でき、range selector の上限は 24 時間でした。ALB の SLO 期間の可用性とエラーバジェット残量は、それぞれ 1 クエリで計算できました。

---

*この記事は自動収集システムによって保存されました。*
