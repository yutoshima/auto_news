---
title: "WASIじゃない、もう一つのインターフェース「WALI」という提案"
source: "Zenn"
category: "it"
published: 2026-10-30T00:45:50
url: https://zenn.dev/progate/articles/wali-webassembly-linux-interface
---

# WASIじゃない、もう一つのインターフェース「WALI」という提案

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月30日 00:45
- **URL**: [https://zenn.dev/progate/articles/wali-webassembly-linux-interface](https://zenn.dev/progate/articles/wali-webassembly-linux-interface)

## 概要

はじめに
最近、仕事でいろんな言語やツールをWebAssembly（wasm）にして、ブラウザーの中で動かすことをやっています。RubyやPython、vimのような、もともとLinuxやMacで動いているプログラムをソースからwasmにビルドする作業です。
このとき毎回悩むのが、ファイルを開く、プロセスを増やす、といった機能をどうするかです。wasmそのものはこうした機能を持っていないので、外から用意してあげる必要があります。よく使われるのは、JavaScriptで用意した関数に任せるEmscriptenと、WASIという標準の関数のセットを使う方法の2つです。
僕はWASIを使う...

---

*この記事は自動収集システムによって保存されました。*
