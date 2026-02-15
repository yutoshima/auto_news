---
title: "圧縮とかtiny codec(Range Coder編)"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-02-15T14:53:52
url: https://qiita.com/mashuel/items/947c994ff4ec82323f5c
---

# 圧縮とかtiny codec(Range Coder編)

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年02月15日 14:53
- **URL**: [https://qiita.com/mashuel/items/947c994ff4ec82323f5c](https://qiita.com/mashuel/items/947c994ff4ec82323f5c)

## 概要

RangeCoder(桁上がり無し版)を少ない文字数で実装しようという魂胆丸見えの企画です。終了判定は記号256で行います。

頻度表上限検査無
関数fが圧縮と展開を担います。Aは数値配列(要素は0～255)、dがfalsyな値なら圧縮処理、さもなければ展開処理。返り値は数...

---

*この記事は自動収集システムによって保存されました。*
