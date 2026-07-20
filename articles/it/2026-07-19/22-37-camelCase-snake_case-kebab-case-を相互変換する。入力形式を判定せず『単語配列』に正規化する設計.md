---
title: "camelCase / snake_case / kebab-case を相互変換する。入力形式を判定せず『単語配列』に正規化する設計"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-19T22:37:52
url: https://qiita.com/sakutto-panda/items/91fb2eb1a2f2338efcd9
---

# camelCase / snake_case / kebab-case を相互変換する。入力形式を判定せず『単語配列』に正規化する設計

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月19日 22:37
- **URL**: [https://qiita.com/sakutto-panda/items/91fb2eb1a2f2338efcd9](https://qiita.com/sakutto-panda/items/91fb2eb1a2f2338efcd9)

## 概要

3行まとめ

変数名を camelCase / snake_case / kebab-case など10種の命名規則に相互変換するツールを作った
設計の肝は 入力形式を判定しないこと。どんな形式でも一度「単語の配列」に正規化してから、目的の規則で再結合する
一番難しいのは...

---

*この記事は自動収集システムによって保存されました。*
