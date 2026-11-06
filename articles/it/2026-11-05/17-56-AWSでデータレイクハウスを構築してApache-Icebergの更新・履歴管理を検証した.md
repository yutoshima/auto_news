---
title: "AWSでデータレイクハウスを構築してApache Icebergの更新・履歴管理を検証した"
source: "Zenn"
category: "it"
published: 2026-11-05T17:56:30
url: https://zenn.dev/kkoch5t2/articles/aws-iceberg-lakehouse-lab
---

# AWSでデータレイクハウスを構築してApache Icebergの更新・履歴管理を検証した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 17:56
- **URL**: [https://zenn.dev/kkoch5t2/articles/aws-iceberg-lakehouse-lab](https://zenn.dev/kkoch5t2/articles/aws-iceberg-lakehouse-lab)

## 概要

AWSでデータレイクハウスを構築する場合、どのようなサービスを組み合わせ、データをどのように管理するのか。まずは全体像を把握したくて、小さな検証環境を作ってみました。
今回はAmazon S3、AWS Glue Data Catalog、Amazon Athena、Apache Icebergを組み合わせ、テーブルの作成からデータの追加・更新・削除、過去のスナップショットの参照（Version Travel）、ファイルの最適化まで一通り試しています。
SQLの実行結果だけでなく、S3上のParquetファイルやメタデータも確認しながら、それぞれのサービスの役割とデータが管理される仕組みを...

---

*この記事は自動収集システムによって保存されました。*
