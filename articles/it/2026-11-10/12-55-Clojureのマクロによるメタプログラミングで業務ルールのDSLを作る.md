---
title: "Clojureのマクロによるメタプログラミングで業務ルールのDSLを作る"
source: "Zenn"
category: "it"
published: 2026-11-10T12:55:14
url: https://zenn.dev/pksha/articles/b7e4c1a9d38f52
---

# Clojureのマクロによるメタプログラミングで業務ルールのDSLを作る

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 12:55
- **URL**: [https://zenn.dev/pksha/articles/b7e4c1a9d38f52](https://zenn.dev/pksha/articles/b7e4c1a9d38f52)

## 概要

要約
設備点検の条件式から、判定関数と、根拠を集めるための参照一覧を生成する DSL(ドメイン固有言語)を作ります。Clojure のマクロで式をデータとして読み取り、参照箇所を集めながら、実行するコードへ変換します。条件式を一度書けば、判定と根拠の収集に必要な定義がそろう仕組みです。
完成したルールと生成コードを見たあと、Clojure の記法とマクロの実装を説明し、ルールの保守・拡張で省ける作業を確認します。Lisp を初めて読む方を想定しています。

 はじめに
PKSHA Technology で AI Research &amp; Solution のソフトウェアエンジニア...

---

*この記事は自動収集システムによって保存されました。*
