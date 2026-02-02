---
title: "gqlkit - TypeScript の型定義と関数から GraphQL Schema を構築するライブラリを作った"
source: "Zenn"
category: "it"
published: 2026-02-01T23:51:18
url: https://zenn.dev/izumin/articles/da27a6dfffba0b
---

# gqlkit - TypeScript の型定義と関数から GraphQL Schema を構築するライブラリを作った

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月01日 23:51
- **URL**: [https://zenn.dev/izumin/articles/da27a6dfffba0b](https://zenn.dev/izumin/articles/da27a6dfffba0b)

## 概要

TypeScript で GraphQL Schema をいい感じに構築できるやつを作ってみたので自慢させてください。
https://github.com/izumin5210/gqlkit
https://gqlkit.izumin.dev/

 何を作ったか（簡単に）
以下のように「TypeScript による型定義」と「define○○ をかぶせた resolver 実装関数」 を export すると、
import type { IDString, NoArgs } from "@gqlkit-ts/runtime";
import { defineQuery, define...

---

*この記事は自動収集システムによって保存されました。*
