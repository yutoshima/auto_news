---
title: "OpenSearch Service の新エンジンがサポートした join、高カーディナリティ集計、query DSL を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-27T13:43:52
url: https://dev.classmethod.jp/articles/opensearch-new-engine-joins-and-dsl/
---

# OpenSearch Service の新エンジンがサポートした join、高カーディナリティ集計、query DSL を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月27日 13:43
- **URL**: [https://dev.classmethod.jp/articles/opensearch-new-engine-joins-and-dsl/](https://dev.classmethod.jp/articles/opensearch-new-engine-joins-and-dsl/)

## 概要

単一ノードの新エンジンドメインで、100 万件のログに対し、PPL と SQL による約 51 万件の span との join、PPL の lookup、distinct な値の集計を実行しました。いずれも 1 秒未満で返り、query DSL の _search も 2 つのクエリで期待どおりの件数を返しました。

---

*この記事は自動収集システムによって保存されました。*
