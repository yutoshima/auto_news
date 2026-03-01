---
title: "GoとRustのざっくり性能比較"
source: "Zenn"
category: "it"
published: 2026-02-28T10:57:53
url: https://zenn.dev/ponyo877/articles/ae398e081464ff
---

# GoとRustのざっくり性能比較

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月28日 10:57
- **URL**: [https://zenn.dev/ponyo877/articles/ae398e081464ff](https://zenn.dev/ponyo877/articles/ae398e081464ff)

## 概要

はじめに
2026年現在のGoとRustの性能差が気になったので調べました。
今回は、標準出力CLI と JSON APIサーバ という2つのパターンで、GoとRustの性能を比較しています。
ビルドの最適化オプションも含めて、LLMの力を借りて出来る限り実用的な観点で検証しています。

 検証環境



項目
バージョン




OS
macOS (darwin/arm64)


Go
1.26.0


Rust
1.93.1



リポジトリはこちらで公開しています:
https://github.com/ponyo877/go-vs-rust
(めっちゃ珍しい言語割合...)
...

---

*この記事は自動収集システムによって保存されました。*
