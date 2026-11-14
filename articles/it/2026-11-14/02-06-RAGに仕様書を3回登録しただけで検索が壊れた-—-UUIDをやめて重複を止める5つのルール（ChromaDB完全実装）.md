---
title: "RAGに仕様書を3回登録しただけで検索が壊れた — UUIDをやめて重複を止める5つのルール（ChromaDB完全実装）"
source: "Qiita (Python)"
category: "it"
published: 2026-11-14T02:06:27
url: https://qiita.com/yukihayama/items/c0015b07916169cbc3e5
---

# RAGに仕様書を3回登録しただけで検索が壊れた — UUIDをやめて重複を止める5つのルール（ChromaDB完全実装）

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月14日 02:06
- **URL**: [https://qiita.com/yukihayama/items/c0015b07916169cbc3e5](https://qiita.com/yukihayama/items/c0015b07916169cbc3e5)

## 概要

自社マニュアルのRAGを運用し始めて2週間、回答の根拠を見たら上位5件が同じ段落のコピーで埋まっていました。仕様書を更新するたびに登録スクリプトを回していた私の失敗です。同じ文書を3回入れた時点で、同じ文章が3重になり、本来ヒットすべき別の章が検索結果から落ちていました。
...

---

*この記事は自動収集システムによって保存されました。*
