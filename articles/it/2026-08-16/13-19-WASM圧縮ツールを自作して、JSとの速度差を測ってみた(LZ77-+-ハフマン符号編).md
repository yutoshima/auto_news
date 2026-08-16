---
title: "WASM圧縮ツールを自作して、JSとの速度差を測ってみた(LZ77 + ハフマン符号編)"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-16T13:19:21
url: https://qiita.com/yukisnow0704/items/13ed96d307473e1fa07a
---

# WASM圧縮ツールを自作して、JSとの速度差を測ってみた(LZ77 + ハフマン符号編)

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月16日 13:19
- **URL**: [https://qiita.com/yukisnow0704/items/13ed96d307473e1fa07a](https://qiita.com/yukisnow0704/items/13ed96d307473e1fa07a)

## 概要

はじめに
以前、RustでWASMを触った際(マンデルブロ集合でJSと速度比較する記事)、「大量データをJSとWASMの間で頻繁にやり取りするとコピーのコストが無視できない」という課題が残りました。
今回はその反省を踏まえて、**「ファイルを1回だけWASMに渡し、圧縮処...

---

*この記事は自動収集システムによって保存されました。*
