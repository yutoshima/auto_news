---
title: "useEffect で API を叩くのを卒業しよう"
source: "Zenn"
category: "it"
published: 2026-02-14T10:57:20
url: https://zenn.dev/ashunar0/articles/32419c3c60cc53
---

# useEffect で API を叩くのを卒業しよう

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月14日 10:57
- **URL**: [https://zenn.dev/ashunar0/articles/32419c3c60cc53](https://zenn.dev/ashunar0/articles/32419c3c60cc53)

## 概要

はじめに
「useEffectでデータ取得するのはやめた方がいい」— こんな話を聞いたことはないだろうか。
でも自分はずっと、useEffect + fetch でAPIを叩いていた。中でtry-catchして、useStateにセットして、ローディングもエラーも自分で管理して。チュートリアルで覚えたそのパターンを、特に疑うこともなく使い続けていた。
「やめた方がいいのは分かった。じゃあ何を使えばいいの？」— この記事は、その疑問に対する自分なりの答えを、実際にTanStack Queryに置き換えてみた過程から書いている。


 useEffect + fetch で書くとこうなる...

---

*この記事は自動収集システムによって保存されました。*
