---
title: "C# 15+の新DIパターン: 内部はinterfaceで疎結合、公開APIはunionで型の許容範囲を制御"
source: "Zenn"
category: "it"
published: 2026-08-08T13:09:58
url: https://zenn.dev/inuinu/articles/csharp15-new-di-interface-union-closed
---

# C# 15+の新DIパターン: 内部はinterfaceで疎結合、公開APIはunionで型の許容範囲を制御

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月08日 13:09
- **URL**: [https://zenn.dev/inuinu/articles/csharp15-new-di-interface-union-closed](https://zenn.dev/inuinu/articles/csharp15-new-di-interface-union-closed)

## 概要

!
【正式版では変わる可能性があります】
この情報は.NET 11.0 preview6で検証していますが、previewなので、
.NET 11やC# 15.0の正式リリース版では違ってくる可能性があります！


 はじめにまとめ

C#15にはunionとclosedが入る
DIにつかうと許容範囲を絞って制限できる
でもテストのためにはinterfaceにもしたい
そんなよくばりができるパターンを紹介

!
💡よくばりパターン
公開APIでは union で受け入れる型を限定しつつ、内部実装では interface を介してテストしやすい構造にする


 unionとDIは相性がいい...

---

*この記事は自動収集システムによって保存されました。*
