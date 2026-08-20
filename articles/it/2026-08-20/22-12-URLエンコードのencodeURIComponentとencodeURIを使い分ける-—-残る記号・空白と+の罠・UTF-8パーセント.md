---
title: "URLエンコードのencodeURIComponentとencodeURIを使い分ける — 残る記号・空白と+の罠・UTF-8パーセント"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-20T22:12:54
url: https://qiita.com/sakutto-panda/items/fc873e5b2aefb79bd4cc
---

# URLエンコードのencodeURIComponentとencodeURIを使い分ける — 残る記号・空白と+の罠・UTF-8パーセント

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月20日 22:12
- **URL**: [https://qiita.com/sakutto-panda/items/fc873e5b2aefb79bd4cc](https://qiita.com/sakutto-panda/items/fc873e5b2aefb79bd4cc)

## 概要

3行まとめ

URLをパーセントエンコード/デコードするブラウザ完結ツールを作った。中身は標準の encodeURIComponent / encodeURI そのままだが、この2つの使い分けが本題

encodeURIComponent はクエリの「値」用、encode...

---

*この記事は自動収集システムによって保存されました。*
