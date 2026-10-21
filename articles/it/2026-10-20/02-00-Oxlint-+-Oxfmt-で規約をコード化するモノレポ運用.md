---
title: "Oxlint + Oxfmt で規約をコード化するモノレポ運用"
source: "Zenn"
category: "it"
published: 2026-10-20T02:00:05
url: https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006
---

# Oxlint + Oxfmt で規約をコード化するモノレポ運用

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月20日 02:00
- **URL**: [https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006](https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006)

## 概要

長らく ESLint + Prettier を使ってきました。大きな不満はなかったものの、実行時間が少し気になっていました。そこで、Biome と Oxc を実際のモノレポで検証して、最終的に Oxlint + Oxfmt に移行しました。
この記事では、Biome と Oxc を比較・検証した過程と、Oxlint + Oxfmt を使ってコーディング規約をコードとして強制する運用を紹介します。

 導入の経緯とモチベーション

 lint / format の待ち時間が気になるようになった
TypeScript の静的解析ツールが TSLint から ESLint に移りつつあった 2...

---

*この記事は自動収集システムによって保存されました。*
