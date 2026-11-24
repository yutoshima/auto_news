---
title: "[Grafana] Ductus で、日付で分けたキー・シングルテーブル設計・GSI などの DynamoDB テーブルを、テーブルを変えずに表示してみました"
source: "DevelopersIO"
category: "it"
published: 2026-11-23T16:47:40
url: https://dev.classmethod.jp/articles/grafana-ductus-dynamodb-date-split-single-table-gsi/
---

# [Grafana] Ductus で、日付で分けたキー・シングルテーブル設計・GSI などの DynamoDB テーブルを、テーブルを変えずに表示してみました

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 16:47
- **URL**: [https://dev.classmethod.jp/articles/grafana-ductus-dynamodb-date-split-single-table-gsi/](https://dev.classmethod.jp/articles/grafana-ductus-dynamodb-date-split-single-table-gsi/)

## 概要

DynamoDB に溜めた時系列データを Grafana で可視化したいというよくあるニーズに対して、既存のテーブル設計を変えずに対応できるツール「Ductus」を使った具体的な方法を紹介します。日付で分けたキー、シングルテーブル設計、GSI など 4 つのテーブル設計パターンを、datasets.yaml の設定だけで Grafana に表示する実例を通じて、実務で気をつけるべきタイムゾーン周りのポイントもお伝えします。

---

*この記事は自動収集システムによって保存されました。*
