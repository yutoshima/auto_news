---
title: "図で理解する Dagster on ECS の構成と、失敗に気づく仕組み"
source: "Zenn"
category: "it"
published: 2026-10-28T03:00:17
url: https://zenn.dev/safie_inc/articles/dagster_on_ecs
---

# 図で理解する Dagster on ECS の構成と、失敗に気づく仕組み

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 03:00
- **URL**: [https://zenn.dev/safie_inc/articles/dagster_on_ecs](https://zenn.dev/safie_inc/articles/dagster_on_ecs)

## 概要

セーフィー株式会社のデータ分析基盤グループでエンジニアをしている渡部です。
セーフィーのデータ分析基盤では、データソースごとにばらばらだったデータ取り込み処理のやり方を揃えるため、Python ライブラリの dlt(data load tool)を採用することとなりました。
dlt は取り込みを実行するだけなので「いつ実行するか？」「失敗にどう気づくか？」の仕組みは別で用意する必要があります。
そこで、オーケストレーションツールとして、Dagster も合わせて導入することとなりました。
現在は、プロダクトの DB から Snowflake へデータを取り込む処理の一部を ECS 上の ...

---

*この記事は自動収集システムによって保存されました。*
