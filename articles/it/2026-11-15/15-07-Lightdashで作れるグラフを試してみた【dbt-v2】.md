---
title: "Lightdashで作れるグラフを試してみた【dbt v2】"
source: "Zenn"
category: "it"
published: 2026-11-15T15:07:26
url: https://zenn.dev/ryatora/articles/lightdash-chart-catalog
---

# Lightdashで作れるグラフを試してみた【dbt v2】

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 15:07
- **URL**: [https://zenn.dev/ryatora/articles/lightdash-chart-catalog](https://zenn.dev/ryatora/articles/lightdash-chart-catalog)

## 概要

1. 概要

 1.1 本記事の目的
NBA（アメリカのプロバスケットボールリーグ）のデータを使って、Lightdash[1]で様々なグラフを作成してみました。各グラフのYAMLも載せています。
2章で準備をして、3章でグラフを種類ごとに作ります。4章では、組み込みにないグラフを作る方法に触れます。

 1.2 Lightdashとは
Lightdashは、dbtのプロジェクトか、Lightdash独自のYAML[2]に書いたmetricなどの定義をもとに、グラフやダッシュボードを作れるオープンソースのBIツールです。本記事ではdbtのプロジェクトを使います。

ディメンション（集計...

---

*この記事は自動収集システムによって保存されました。*
