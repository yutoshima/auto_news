---
title: "Vanilla CSSでもデザインシステムを構築したい！：css-var-kitによるtype-awareな補完とLint"
source: "Zenn"
category: "it"
published: 2026-04-06T02:14:43
url: https://zenn.dev/jo16oh/articles/fa8080edc388b3
---

# Vanilla CSSでもデザインシステムを構築したい！：css-var-kitによるtype-awareな補完とLint

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月06日 02:14
- **URL**: [https://zenn.dev/jo16oh/articles/fa8080edc388b3](https://zenn.dev/jo16oh/articles/fa8080edc388b3)

## 概要

css-var-kitというツールを開発したので、ご紹介します。
css-var-kitは、CSS変数を扱うための軽量で高速なRust製ツールキットです。CSS変数に特化したLinterと、Language Serverを備えています。変数の値の型を認識することで、プロパティの定義に適合しない型の変数が使用されるのを防いだり、補完候補を絞り込んだりすることができます。

 インストール
npmまたはcargoからインストールできます。
npm install -D css-var-kit
cargo install css-var-kit

 機能
css-var-kitはLinterと...

---

*この記事は自動収集システムによって保存されました。*
