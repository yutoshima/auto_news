---
title: "メモリに載らないGROUP BYをDuckDBはどう処理するのか"
source: "Zenn"
category: "it"
published: 2026-09-10T01:42:07
url: https://zenn.dev/loglass/articles/7c140c6689d8c2
---

# メモリに載らないGROUP BYをDuckDBはどう処理するのか

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月10日 01:42
- **URL**: [https://zenn.dev/loglass/articles/7c140c6689d8c2](https://zenn.dev/loglass/articles/7c140c6689d8c2)

## 概要

!
この記事は毎週必ず記事がでるテックブログ Loglass Tech Blog Sprint の160週目の記事です！4年連続達成まであと52週となりました！

ログラスの龍島(@hryushm)です。先日スイカを一玉いただく機会があったのですが、とても大きいので一度に全部は食べきれず、切り分けて冷蔵庫に入れて数日かけて食べました。ということで今日はメモリに載りきらないデータの処理方法の話です。

 はじめに
先日、DuckDBの開発元であるDuckLabsがAWSに加わることが発表されました[1]。そのDuckDBは、メモリより大きなデータを扱うのが得意だと言われます。公式ドキュメン...

---

*この記事は自動収集システムによって保存されました。*
