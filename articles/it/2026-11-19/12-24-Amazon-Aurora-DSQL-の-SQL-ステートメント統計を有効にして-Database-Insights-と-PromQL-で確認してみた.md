---
title: "Amazon Aurora DSQL の SQL ステートメント統計を有効にして Database Insights と PromQL で確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T12:24:08
url: https://dev.classmethod.jp/articles/aurora-dsql-statement-statistics/
---

# Amazon Aurora DSQL の SQL ステートメント統計を有効にして Database Insights と PromQL で確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 12:24
- **URL**: [https://dev.classmethod.jp/articles/aurora-dsql-statement-statistics/](https://dev.classmethod.jp/articles/aurora-dsql-statement-statistics/)

## 概要

update-cluster で STATEMENT_STATISTICS を指定すると、SQL ごとの所要時間、実行回数、DPU を取得できます。影響の大きな SQL を特定でき、SQL やインデックスの改善対象を見つけるのに役立ちます。Aurora DSQL の追加料金はかかりません。

---

*この記事は自動収集システムによって保存されました。*
