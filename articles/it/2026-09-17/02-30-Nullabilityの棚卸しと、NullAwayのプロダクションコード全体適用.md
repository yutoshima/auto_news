---
title: "Nullabilityの棚卸しと、NullAwayのプロダクションコード全体適用"
source: "Zenn"
category: "it"
published: 2026-09-17T02:30:05
url: https://zenn.dev/nstock/articles/null-away-20260917
---

# Nullabilityの棚卸しと、NullAwayのプロダクションコード全体適用

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月17日 02:30
- **URL**: [https://zenn.dev/nstock/articles/null-away-20260917](https://zenn.dev/nstock/articles/null-away-20260917)

## 概要

これはなに
Nstock株式会社でソフトウェアエンジニアをしているnonoです。主に携わっているNstock株式報酬のバックエンドサービスにNullAwayを導入しました。
不確実なNullabilityはレビューコストを常に引き上げる方向に働きます。NullAwayはアノテーションベースに静的解析を行ない、不適切な取り扱いをコンパイルエラーとして検出します。これによりJavaでもnull-safeな言語のように実装できます。コードの実装コストが低廉化した現在において、受入のコストを下げる重要度は高いと考えて導入しました。
NullAwayを設定だけ導入することは簡単です。難しいのは...

---

*この記事は自動収集システムによって保存されました。*
