---
title: "pgvectorの距離を類似度に直して根拠不足を判定する：RAG検索層とpytest回帰"
source: "Qiita トレンド"
category: "it"
published: 2026-11-14T00:00:08
url: https://qiita.com/takumi_engineer/items/93db73ccf114bad454f1?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items
---

# pgvectorの距離を類似度に直して根拠不足を判定する：RAG検索層とpytest回帰

## メタデータ

- **情報源**: Qiita トレンド
- **カテゴリ**: it
- **公開日時**: 2026年11月14日 00:00
- **URL**: [https://qiita.com/takumi_engineer/items/93db73ccf114bad454f1?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items](https://qiita.com/takumi_engineer/items/93db73ccf114bad454f1?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

## 概要

解きたい問題
RAGで「根拠が弱ければ回答を控える」判定を入れようとして、最初につまずくのがスコアの向きです。pgvectorが返すのは距離で、類似度ではありません。
距離のまま閾値に使うと、大小の判定が逆になります。本記事では、検索SQLで類似度に変換して返す層と、判定...

---

*この記事は自動収集システムによって保存されました。*
