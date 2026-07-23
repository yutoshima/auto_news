---
title: "WebエディタのTab問題について調べてみた"
source: "Zenn"
category: "it"
published: 2026-07-22T03:36:06
url: https://zenn.dev/cybozu_frontend/articles/contenteditable-tab
---

# WebエディタのTab問題について調べてみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月22日 03:36
- **URL**: [https://zenn.dev/cybozu_frontend/articles/contenteditable-tab](https://zenn.dev/cybozu_frontend/articles/contenteditable-tab)

## 概要

この記事は、CYBOZU SUMMER BLOG FES '26の記事です。
こんにちは！26卒でフロントエンドエンジニア職として入社したコサキンです。
内定者バイトでもお世話になった kintone のチームに配属され、わいわい働いています。
今回はWebエディタでのTab 入力時の挙動が気になったので、調べてみました。

 今回気になったこと
エディタでは Tab を入力すると、\t や複数のスペースが入力されるケースが多いと思います。
しかし、ブラウザでは Tab 入力にフォーカスの移動が割り当てられているため、単純に Tab を入力に置き換えると、エディタから抜けられなくなる問題...

---

*この記事は自動収集システムによって保存されました。*
