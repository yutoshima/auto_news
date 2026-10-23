---
title: "Claude CodeやCodexで並列開発していたら、Macのストレージが残り8GBになったので掃除した"
source: "Zenn"
category: "it"
published: 2026-10-22T17:21:33
url: https://zenn.dev/yoshinani_dev/articles/0c17dec1c082a1
---

# Claude CodeやCodexで並列開発していたら、Macのストレージが残り8GBになったので掃除した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 17:21
- **URL**: [https://zenn.dev/yoshinani_dev/articles/0c17dec1c082a1](https://zenn.dev/yoshinani_dev/articles/0c17dec1c082a1)

## 概要

!
クライアント案件のリポジトリ名は伏せています。容量の数字は、dfとduで実際に測った値です。

1TBのMacBook Airで、ストレージの空きが8GBまで減っていました。
Claude Codeに「ストレージがほぼないので整理したい」と頼んで、何が容量を使っているかを調べてもらいながら掃除しました。原因はほとんどが開発まわりで、最終的に空きは約380GBまで戻りました。
最近はClaude CodeやCodexに作業を並列でお願いすることが多く、そのたびにGitのworktreeが作られます。このやり方だと溜まりやすいものがいくつか分かったので、消した順に紹介します。

 何が容...

---

*この記事は自動収集システムによって保存されました。*
