---
title: "TanStack Query × Dexie.js で「プロトタイプを全部捨てる」から卒業する境界設計"
source: "Zenn"
category: "it"
published: 2026-05-25T09:30:05
url: https://zenn.dev/dress_code/articles/5d33f06aa14582
---

# TanStack Query × Dexie.js で「プロトタイプを全部捨てる」から卒業する境界設計

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月25日 09:30
- **URL**: [https://zenn.dev/dress_code/articles/5d33f06aa14582](https://zenn.dev/dress_code/articles/5d33f06aa14582)

## 概要

はじめに
こんにちは、Dress Code株式会社でプロダクトエンジニアをしているもず（@mozu1206）です。
データ構造やAPI設計までしっかりやる時間はないけれど、ビジネスサイドと「作成・更新・削除まで動く画面」で会話を進めたい場面、ありませんか？AIで雑にプロトタイプを作る選択肢もありますが、本実装に入るときに全部捨てるのは、正直もったいないですよね。
この記事では、フロントのみでプロトタイプを作りつつ、API繋ぎ込み時に捨てるコードを最小限にする設計（-api → -query → コンポーネントの3層構造）を紹介します。

 TL;DR

-api 層にデータのやりとり...

---

*この記事は自動収集システムによって保存されました。*
