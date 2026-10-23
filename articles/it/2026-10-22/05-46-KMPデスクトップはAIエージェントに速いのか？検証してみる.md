---
title: "KMPデスクトップはAIエージェントに速いのか？検証してみる"
source: "Zenn"
category: "it"
published: 2026-10-22T05:46:57
url: https://zenn.dev/shogo/articles/f847c35ea8dccb
---

# KMPデスクトップはAIエージェントに速いのか？検証してみる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 05:46
- **URL**: [https://zenn.dev/shogo/articles/f847c35ea8dccb](https://zenn.dev/shogo/articles/f847c35ea8dccb)

## 概要

はじめに
この記事 を読みました。
AI エージェントにアプリを操作させて動作を確認するとき、Android エミュレータではなく Kotlin Multiplatform のデスクトップ版を使った方が速い、という内容です。記事には実測値も載っています。



エージェントがアプリを操作する方式
1 件あたり




Android エミュレータ（Android CLI の layout + adb）
5.68 秒


Android エミュレータ（生の UIAutomator + adb）
4.14 秒


デスクトップ（Compose MCP）
0.60 秒


デスクトップ（U...

---

*この記事は自動収集システムによって保存されました。*
