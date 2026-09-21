---
title: "AWS Glue Zero-ETL、ターゲットテーブルの所有権と競合検出を追加"
source: "AWS What's New"
category: "it"
published: 2026-09-14T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/glue-zero-etl-ownership-conflicts/
---

# AWS Glue Zero-ETL、ターゲットテーブルの所有権と競合検出を追加

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月14日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/glue-zero-etl-ownership-conflicts/](https://aws.amazon.com/about-aws/whats-new/2026/09/glue-zero-etl-ownership-conflicts/)

## 概要

AWS GlueのゼロETL統合は、テーブルのプロパティ衝突を検出し、統合の所有権を追跡します。ソーステーブルとターゲットカタログを設定すると、Glueは作成されるテーブルのプロパティを所有者となる統合に関連付けるため、2つの統合があなたの知らないうちに同じターゲットテーブルを指すことはできなくなります。これは、Amazon S3 TablesとSageMaker Lakehouseカタログの間で機能します。

データチームが複数のゼロETL統合を実行する場合、それぞれのソースの配置場所を予測可能に管理できます。

---

*この記事は自動収集システムによって保存されました。*
