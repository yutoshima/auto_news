---
title: "[小ネタ] Amazon RDSをIaCで作成する際は EnablePerformanceInsights = true にしておいた方が良いはなし"
source: "DevelopersIO"
category: "it"
published: 2026-10-28T10:53:56
url: https://dev.classmethod.jp/articles/amazon-rds-still-require-enableperfomanceinsights-true/
---

# [小ネタ] Amazon RDSをIaCで作成する際は EnablePerformanceInsights = true にしておいた方が良いはなし

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 10:53
- **URL**: [https://dev.classmethod.jp/articles/amazon-rds-still-require-enableperfomanceinsights-true/](https://dev.classmethod.jp/articles/amazon-rds-still-require-enableperfomanceinsights-true/)

## 概要

Performance Insights廃止後のIaCを使ったRDS環境構築時に遭遇した経験を共有します。EnablePerformanceInsightsパラメーターの役割変化により、Database Insightsのメトリクス収集が無効になってしまった事象と対応策をまとめました。

---

*この記事は自動収集システムによって保存されました。*
