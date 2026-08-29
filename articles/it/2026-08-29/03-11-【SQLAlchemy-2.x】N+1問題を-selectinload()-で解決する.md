---
title: "【SQLAlchemy 2.x】N+1問題を selectinload() で解決する"
source: "Qiita (Python)"
category: "it"
published: 2026-08-29T03:11:47
url: https://qiita.com/windingroad_engineer/items/3adc4cd5a36a50e4fd08
---

# 【SQLAlchemy 2.x】N+1問題を selectinload() で解決する

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月29日 03:11
- **URL**: [https://qiita.com/windingroad_engineer/items/3adc4cd5a36a50e4fd08](https://qiita.com/windingroad_engineer/items/3adc4cd5a36a50e4fd08)

## 概要

こんにちは。
SQLAlchemyでORMを使い始めると、「記事一覧を取得しただけなのに、なぜかSQLが大量に発行されている」という場面に遭遇することがあります。
その原因の多くがN+1問題です。データ量が少ない開発環境では気付きにくいものの、本番環境ではパフォーマンス低下...

---

*この記事は自動収集システムによって保存されました。*
