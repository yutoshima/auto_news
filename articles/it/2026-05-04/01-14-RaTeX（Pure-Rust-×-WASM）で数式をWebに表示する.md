---
title: "RaTeX（Pure Rust × WASM）で数式をWebに表示する"
source: "Zenn"
category: "it"
published: 2026-05-04T01:14:06
url: https://zenn.dev/dannchu/articles/ratex-wasm-math-renderer
---

# RaTeX（Pure Rust × WASM）で数式をWebに表示する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月04日 01:14
- **URL**: [https://zenn.dev/dannchu/articles/ratex-wasm-math-renderer](https://zenn.dev/dannchu/articles/ratex-wasm-math-renderer)

## 概要

RaTeX とは
RaTeX は Pure Rust で書かれた KaTeX 互換の数式レンダラーです。WebAssembly（WASM）にコンパイルされ、ブラウザ上で LaTeX 数式を canvas に描画する Web Component として使えます。

KaTeX の LaTeX 構文をほぼそのまま使える

\ce{} による化学式、\pu{} による単位表記にも対応
npm CDN から1行で読み込むだけで利用可能

デモサイトを公開しています：
https://shimizudan.github.io/20260504ratex/


 基本的な使い方
&lt;!-- ...

---

*この記事は自動収集システムによって保存されました。*
