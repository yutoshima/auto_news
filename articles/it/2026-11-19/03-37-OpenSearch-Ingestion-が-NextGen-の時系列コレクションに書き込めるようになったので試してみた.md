---
title: "OpenSearch Ingestion が NextGen の時系列コレクションに書き込めるようになったので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T03:37:04
url: https://dev.classmethod.jp/articles/osis-nextgen-timeseries-collection-sink/
---

# OpenSearch Ingestion が NextGen の時系列コレクションに書き込めるようになったので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 03:37
- **URL**: [https://dev.classmethod.jp/articles/osis-nextgen-timeseries-collection-sink/](https://dev.classmethod.jp/articles/osis-nextgen-timeseries-collection-sink/)

## 概要

Amazon OpenSearch Ingestion (OSIS) のパイプラインから NextGen の時系列コレクションへ、追加の引数なしで書き込めました。timestamp が欠けたドキュメントは、コレクションへの直接書き込みでは拒否され、OSIS 経由では取り込み時刻が入って保存されました。

---

*この記事は自動収集システムによって保存されました。*
