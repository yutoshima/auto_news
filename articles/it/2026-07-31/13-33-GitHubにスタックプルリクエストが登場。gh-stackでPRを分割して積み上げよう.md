---
title: "GitHubにスタックプルリクエストが登場。gh stackでPRを分割して積み上げよう"
source: "Zenn"
category: "it"
published: 2026-07-31T13:33:10
url: https://zenn.dev/ubie_dev/articles/gh-stack-introduction
---

# GitHubにスタックプルリクエストが登場。gh stackでPRを分割して積み上げよう

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月31日 13:33
- **URL**: [https://zenn.dev/ubie_dev/articles/gh-stack-introduction](https://zenn.dev/ubie_dev/articles/gh-stack-introduction)

## 概要

GitHubでPRを細かく作り、前のブランチに対して数珠つなぎのようにPRを作る私が大歓喜！ GitHubに「スタックプルリクエスト」機能が来ました💐

 3行まとめ

大きな変更を、順序付きの小さなPR群（スタック）に分割して扱える機能がGitHub公式で登場

gh extension install github/gh-stackでCLIから使える

gh stack syncでスタックのrebase, pushまで一発でできる


 巨大な1つのプルリクエストは悪
AIエージェントでの開発が前提の現在、AIエージェントは素早く多くのコードを生み出します。気をつけないと、1つのプル...

---

*この記事は自動収集システムによって保存されました。*
