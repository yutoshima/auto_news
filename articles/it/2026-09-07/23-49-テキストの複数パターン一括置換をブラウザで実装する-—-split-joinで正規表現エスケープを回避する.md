---
title: "テキストの複数パターン一括置換をブラウザで実装する — split/joinで正規表現エスケープを回避する"
source: "Qiita (React)"
category: "it"
published: 2026-09-07T23:49:25
url: https://qiita.com/sakutto-panda/items/35004059284557c72c64
---

# テキストの複数パターン一括置換をブラウザで実装する — split/joinで正規表現エスケープを回避する

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年09月07日 23:49
- **URL**: [https://qiita.com/sakutto-panda/items/35004059284557c72c64](https://qiita.com/sakutto-panda/items/35004059284557c72c64)

## 概要

3行まとめ

検索・置換ルールを複数登録し、1回の操作でテキストへ順番に適用するブラウザ完結ツールを作った
通常モード（文字列一致）は正規表現を一切使わず split(search).join(replace) で実装。. や ( のような正規表現の特殊文字をエスケープす...

---

*この記事は自動収集システムによって保存されました。*
