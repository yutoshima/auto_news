---
title: "GitHub rulesetのON/OFFで「マージ禁止期間」を作る"
source: "Zenn"
category: "it"
published: 2026-11-10T02:45:29
url: https://zenn.dev/yesodco/articles/yesod-github-ruleset-merge-freeze
---

# GitHub rulesetのON/OFFで「マージ禁止期間」を作る

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 02:45
- **URL**: [https://zenn.dev/yesodco/articles/yesod-github-ruleset-merge-freeze](https://zenn.dev/yesodco/articles/yesod-github-ruleset-merge-freeze)

## 概要

こんにちは、株式会社イエソドでバックエンドエンジニアをしているik-fib（@ik11235）です。

 はじめに
弊社では、週の初めにリリース対象の変更内容を確認する「リリース判定」を行っています。この記事では、リリースする変更をまとめるブランチをGit flowにならって仮にdevelopと呼びます。リリースまでの流れは次のとおりです。

普段の開発では、レビューと検証を通った変更をdevelopにマージする
週の初めに、developに入っている変更内容をリリース判定で確認する
判定を通った変更をリリースするため、developからリリースブランチを作成する

問題は、リリース判定...

---

*この記事は自動収集システムによって保存されました。*
