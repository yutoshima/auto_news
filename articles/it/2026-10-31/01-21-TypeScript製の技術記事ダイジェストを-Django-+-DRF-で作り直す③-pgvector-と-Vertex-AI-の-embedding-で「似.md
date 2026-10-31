---
title: "TypeScript製の技術記事ダイジェストを Django + DRF で作り直す③:pgvector と Vertex AI の embedding で「似てる記事」と意味検索を作る"
source: "Qiita (Python)"
category: "it"
published: 2026-10-31T01:21:06
url: https://qiita.com/yukisnow0704/items/f720b12b0d5bdad55115
---

# TypeScript製の技術記事ダイジェストを Django + DRF で作り直す③:pgvector と Vertex AI の embedding で「似てる記事」と意味検索を作る

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月31日 01:21
- **URL**: [https://qiita.com/yukisnow0704/items/f720b12b0d5bdad55115](https://qiita.com/yukisnow0704/items/f720b12b0d5bdad55115)

## 概要

はじめに
前回は管理コマンド ingest を作りました。RSS から記事を取り込み、Vertex AI の Gemini で要約とカテゴリを付けるところまでです。
今回は記事を embedding(ベクトル) に変換して PostgreSQL の pgvector に保...

---

*この記事は自動収集システムによって保存されました。*
