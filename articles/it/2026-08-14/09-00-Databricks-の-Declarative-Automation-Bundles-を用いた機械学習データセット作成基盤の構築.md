---
title: "Databricks の Declarative Automation Bundles を用いた機械学習データセット作成基盤の構築"
source: "Zenn"
category: "it"
published: 2026-08-14T09:00:05
url: https://zenn.dev/colum2131/articles/46b5560dce0e3a
---

# Databricks の Declarative Automation Bundles を用いた機械学習データセット作成基盤の構築

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月14日 09:00
- **URL**: [https://zenn.dev/colum2131/articles/46b5560dce0e3a](https://zenn.dev/colum2131/articles/46b5560dce0e3a)

## 概要

チューリングの MLOps エンジニアの岩政です。
チューリングでは、センサ入力から車両の将来の行動を一貫して推定する学習ベースのモデルとして End-to-End (E2E) 自動運転 AI を開発しています。E2E 自動運転 AI の学習にはデータセットが必要です。私の所属する MLOps チームが、これを作成するためのデータ基盤の開発を行っています。
MLOps チームでは車両に搭載したカメラなどのセンサから走行データを収集し、Data Lake に格納しています。更に ETL (Extract, Transform, Load) パイプラインを通じて、数千時間以上の走行データに相...

---

*この記事は自動収集システムによって保存されました。*
