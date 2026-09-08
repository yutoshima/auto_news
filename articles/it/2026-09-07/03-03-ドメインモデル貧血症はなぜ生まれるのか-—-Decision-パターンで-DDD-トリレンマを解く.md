---
title: "ドメインモデル貧血症はなぜ生まれるのか — Decision パターンで DDD トリレンマを解く"
source: "Zenn"
category: "it"
published: 2026-09-07T03:03:17
url: https://zenn.dev/tellernovel_inc/articles/0193eb68cabb6e
---

# ドメインモデル貧血症はなぜ生まれるのか — Decision パターンで DDD トリレンマを解く

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月07日 03:03
- **URL**: [https://zenn.dev/tellernovel_inc/articles/0193eb68cabb6e](https://zenn.dev/tellernovel_inc/articles/0193eb68cabb6e)

## 概要

テラーノベルで Go を書いている typer です。
この記事は次のような方向けです。

Go でコードを書いていて、domain 層にロジックが集まらないと感じている方
DDD の戦術的パターンを入れてみたが、結局 domain の外側にロジックが溜まっている方
リポジトリを呼ぶために domain に context と error を持ち込むかどうかで迷ったことがある方

先に結論を書いておきます。

ドメインモデル貧血症は、怠慢ではなく構造的なトリレンマの結果として生まれやすい
「判断するために何が要るか」を型で返せば、型の制約を保ちながらトリレンマは解ける


 「戦術的 D...

---

*この記事は自動収集システムによって保存されました。*
