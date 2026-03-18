---
title: "手動 ER 図メンテから卒業する── GitHub Actions × DBML 自動生成の実践"
source: "Zenn"
category: "it"
published: 2026-03-18T00:00:13
url: https://zenn.dev/finatext/articles/auto-generate-dbml-from-orm
---

# 手動 ER 図メンテから卒業する── GitHub Actions × DBML 自動生成の実践

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年03月18日 00:00
- **URL**: [https://zenn.dev/finatext/articles/auto-generate-dbml-from-orm](https://zenn.dev/finatext/articles/auto-generate-dbml-from-orm)

## 概要

こんにちは、ナウキャストで LLM エンジニアをしている Ryotaro です。
バックエンドの ER 図、ちゃんとメンテナンスできていますか？
「コードは変えたけど ER 図の更新を忘れた」「いつの間にかドキュメントが実態と乖離していた」という経験は、多くのエンジニアに心当たりがあるのではないでしょうか。
この記事では、SQLAlchemy モデルを Single Source of Truth（SSoT）として、GitHub Actions で DBML を自動生成・コミットする仕組みを構築しました。やってみたら結構うまくハマったので、その方法を紹介します。開発者はコードだけ修正すれ...

---

*この記事は自動収集システムによって保存されました。*
