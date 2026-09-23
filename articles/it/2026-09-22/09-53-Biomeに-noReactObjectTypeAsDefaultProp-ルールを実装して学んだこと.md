---
title: "Biomeに noReactObjectTypeAsDefaultProp ルールを実装して学んだこと"
source: "Zenn"
category: "it"
published: 2026-09-22T09:53:21
url: https://zenn.dev/subaru_hello/articles/biome-rust-first-contribution
---

# Biomeに noReactObjectTypeAsDefaultProp ルールを実装して学んだこと

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月22日 09:53
- **URL**: [https://zenn.dev/subaru_hello/articles/biome-rust-first-contribution](https://zenn.dev/subaru_hello/articles/biome-rust-first-contribution)

## 概要

BiomeにnoReactObjectTypeAsDefaultPropというlintルールを追加しました。

Issue #7656
Pull Request #10634

eslint-plugin-reactのno-object-type-as-default-propをBiomeへ移植するissueを担当したものです。
この記事では、追加したルールの仕組みと、実装やレビューを通して学んだRustについてまとめます。

 追加したルール
今回追加したルールは、次のような式がpropsのデフォルト値に使われていないかを検査しています。
function Component({ it...

---

*この記事は自動収集システムによって保存されました。*
