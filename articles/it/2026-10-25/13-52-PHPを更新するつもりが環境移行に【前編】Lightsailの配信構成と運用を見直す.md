---
title: "PHPを更新するつもりが環境移行に【前編】Lightsailの配信構成と運用を見直す"
source: "Zenn"
category: "it"
published: 2026-10-25T13:52:37
url: https://zenn.dev/hotaka_noda/articles/3b4c51ecfe561d
---

# PHPを更新するつもりが環境移行に【前編】Lightsailの配信構成と運用を見直す

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 13:52
- **URL**: [https://zenn.dev/hotaka_noda/articles/3b4c51ecfe561d](https://zenn.dev/hotaka_noda/articles/3b4c51ecfe561d)

## 概要

はじめに
PHPの脆弱性に対応しようとしたら、WordPressの環境移行が必要になりました。
先日、PHPの脆弱性対応を行った際に、利用していた環境の制約から、WordPressを新しい環境へ移すことになりました。
実行環境にはAmazon Lightsailを使っています。Lightsailは、仮想サーバーやストレージなどを月額料金のプランで利用できるAWSのサービスです。WordPressなどがあらかじめ組み込まれたブループリントを選び、サイトの実行環境を作れます。
今回使っていたのはBitnami版WordPressです。通常のパッケージ更新ではPHPが更新されず、ブループリ...

---

*この記事は自動収集システムによって保存されました。*
