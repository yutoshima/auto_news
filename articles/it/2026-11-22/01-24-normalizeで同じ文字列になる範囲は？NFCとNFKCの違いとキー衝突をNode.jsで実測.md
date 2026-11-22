---
title: "normalizeで同じ文字列になる範囲は？NFCとNFKCの違いとキー衝突をNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-22T01:24:33
url: https://qiita.com/ennagara128/items/fe9e35d4c2324fd4fd69
---

# normalizeで同じ文字列になる範囲は？NFCとNFKCの違いとキー衝突をNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月22日 01:24
- **URL**: [https://qiita.com/ennagara128/items/fe9e35d4c2324fd4fd69](https://qiita.com/ennagara128/items/fe9e35d4c2324fd4fd69)

## 概要

同じ「が」に見えても、JavaScript の === で一致しないことがあります。結合文字を含む入力を比較するなら normalize('NFC') が候補ですが、NFKC に変えると丸数字まで普通の数字になります。検索用に揃える範囲と、元の表記として残す範囲を分けて考え...

---

*この記事は自動収集システムによって保存されました。*
