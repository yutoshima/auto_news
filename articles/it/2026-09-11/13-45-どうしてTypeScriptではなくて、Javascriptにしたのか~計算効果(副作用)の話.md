---
title: "どうしてTypeScriptではなくて、Javascriptにしたのか~計算効果(副作用)の話"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-09-11T13:45:45
url: https://qiita.com/take37/items/6e093178909ea10858a3
---

# どうしてTypeScriptではなくて、Javascriptにしたのか~計算効果(副作用)の話

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年09月11日 13:45
- **URL**: [https://qiita.com/take37/items/6e093178909ea10858a3](https://qiita.com/take37/items/6e093178909ea10858a3)

## 概要

はじめに
Discordの通話の状態をSlackに知らせるBotを最近つくりました。
こんな感じのイメージのもの

GitHubのリンク

このプログラム自体は小さめです。しかし、読み返してみたときに、計算効果について考える上で良い題材な気がしたのでまとめてみます。
これ...

---

*この記事は自動収集システムによって保存されました。*
