---
title: "Pokémon GO Plus + を分解して、ポケモンスリープの睡眠計測を自動化する装置を作った"
source: "Zenn"
category: "it"
published: 2026-09-22T09:17:48
url: https://zenn.dev/koichi73/articles/pokemon-go-plus-teardown-esp32
---

# Pokémon GO Plus + を分解して、ポケモンスリープの睡眠計測を自動化する装置を作った

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月22日 09:17
- **URL**: [https://zenn.dev/koichi73/articles/pokemon-go-plus-teardown-esp32](https://zenn.dev/koichi73/articles/pokemon-go-plus-teardown-esp32)

## 概要

はじめに
以前こんなものを作りました。
https://x.com/Koichi73_/status/2100180485985226755
ポケモンスリープの計測に使う「Pokémon GO Plus +」を分解して、スマホから計測を開始・終了できるようにしたものです。
そこからさらに改良して、振動モーターで揺らすことで、自分の睡眠とは関係なく、狙いどおりの睡眠データを出せるようになりました。

うとうと・すやすや・ぐっすりを 33%・33%・34% で指定して、一晩動かした結果
今回はこれを紹介します。
!
本記事は、個人開発として試した結果の紹介です。この遊び方を推奨するもので...

---

*この記事は自動収集システムによって保存されました。*
