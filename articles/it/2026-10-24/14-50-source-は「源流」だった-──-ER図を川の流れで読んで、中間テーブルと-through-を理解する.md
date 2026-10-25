---
title: "source は「源流」だった ── ER図を川の流れで読んで、中間テーブルと through を理解する"
source: "Qiita トレンド"
category: "it"
published: 2026-10-24T14:50:36
url: https://qiita.com/mmsbox/items/f2950c2690150264353b?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items
---

# source は「源流」だった ── ER図を川の流れで読んで、中間テーブルと through を理解する

## メタデータ

- **情報源**: Qiita トレンド
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 14:50
- **URL**: [https://qiita.com/mmsbox/items/f2950c2690150264353b?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items](https://qiita.com/mmsbox/items/f2950c2690150264353b?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

## 概要

はじめに
Railsで「お気に入り」や「いいね」を作るとき、こんなコードを書きます。
has_many :favorites
has_many :favorite_books, through: :favorites, source: :book

私は最初、この2行目を...

---

*この記事は自動収集システムによって保存されました。*
