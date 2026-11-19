---
title: "Creators APIのSearchItemsで、カテゴリーごとに必要な数だけ商品を取る（itemCountとitemPageはどちらも1〜10）"
source: "Qiita (Python)"
category: "it"
published: 2026-11-19T02:58:42
url: https://qiita.com/REALINE/items/4c60305cd89cce5a2bc2
---

# Creators APIのSearchItemsで、カテゴリーごとに必要な数だけ商品を取る（itemCountとitemPageはどちらも1〜10）

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 02:58
- **URL**: [https://qiita.com/REALINE/items/4c60305cd89cce5a2bc2](https://qiita.com/REALINE/items/4c60305cd89cce5a2bc2)

## 概要

AmazonのCreators APIの SearchItems は、1回のリクエストで10件までしか返しません。複数のカテゴリーから「合計20件、1カテゴリーは多くても7件」のように取るには、ページを送りながら、カテゴリーごとの続きの位置を覚えておく必要があります。
カテ...

---

*この記事は自動収集システムによって保存されました。*
