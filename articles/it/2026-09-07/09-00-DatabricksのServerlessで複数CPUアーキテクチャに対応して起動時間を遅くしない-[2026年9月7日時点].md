---
title: "DatabricksのServerlessで複数CPUアーキテクチャに対応して起動時間を遅くしない [2026年9月7日時点]"
source: "Zenn"
category: "it"
published: 2026-09-07T09:00:08
url: https://zenn.dev/turing_motors/articles/71a4dd39e0654c
---

# DatabricksのServerlessで複数CPUアーキテクチャに対応して起動時間を遅くしない [2026年9月7日時点]

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月07日 09:00
- **URL**: [https://zenn.dev/turing_motors/articles/71a4dd39e0654c](https://zenn.dev/turing_motors/articles/71a4dd39e0654c)

## 概要

チューリングの MLOps エンジニアの岩政です。
以前、Databricks の Declarative Automation Bundles を用いた機械学習データセット作成基盤の構築をまとめました。この記事はその続きにあたるので、まだご覧になっていない方は先に読んでいただけると嬉しいです。
https://zenn.dev/turing_motors/articles/46b5560dce0e3a
この中で「4.5.2 Python のライブラリの依存解決を高速にする」を紹介しました。
Databricks の Serverless compute では、依存パッケージのインストー...

---

*この記事は自動収集システムによって保存されました。*
