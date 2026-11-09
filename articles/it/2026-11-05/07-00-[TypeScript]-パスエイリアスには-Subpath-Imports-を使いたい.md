---
title: "[TypeScript] パスエイリアスには Subpath Imports を使いたい"
source: "Zenn"
category: "it"
published: 2026-11-05T07:00:05
url: https://zenn.dev/mediba/articles/167e2a3f663889
---

# [TypeScript] パスエイリアスには Subpath Imports を使いたい

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 07:00
- **URL**: [https://zenn.dev/mediba/articles/167e2a3f663889](https://zenn.dev/mediba/articles/167e2a3f663889)

## 概要

medibaにバックエンドエンジニアとして所属している@mdbr92です。
肩書はバックエンドエンジニアですが、実際にはフロントエンド・API・バッチ処理などアプリケーション全体の開発やアーキテクチャ選定・開発環境の整備などをよく担当しています。

 はじめに
私がこれまで開発に携わったTypeScriptを採用したいくつかのプロダクトでは、tsconfig.json の paths を使ったパスエイリアス設定を利用しています。
パスエイリアス設定を利用して、たとえば ../../../../lib/log.ts のような相対パスでimport文を記述した際の指定ミスや可読性低下を避け、...

---

*この記事は自動収集システムによって保存されました。*
