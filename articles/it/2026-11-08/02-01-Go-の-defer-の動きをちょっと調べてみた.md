---
title: "Go の defer の動きをちょっと調べてみた"
source: "Zenn"
category: "it"
published: 2026-11-08T02:01:23
url: https://zenn.dev/wakame_atsushi/articles/8c45ac07bac534
---

# Go の defer の動きをちょっと調べてみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月08日 02:01
- **URL**: [https://zenn.dev/wakame_atsushi/articles/8c45ac07bac534](https://zenn.dev/wakame_atsushi/articles/8c45ac07bac534)

## 概要

defer の動作について見ていきます。
コードはすべて go1.27.3（windows/amd64）で確認しています。

 登録と実行は別のタイミング
defer には、「後で呼ぶ内容を保存する」と「保存した内容を呼び出す」という2つの段階があります。
この記事では、前者を登録、後者を実行と呼びます。
言語仕様の Defer statements は、defer 文を実行するたびに、呼び出す関数値と引数を通常どおり評価して新しく保存し、関数そのものはまだ呼ばない、と定めています。
これをコードで確かめます。
func evalTiming() {
	i := 0
	defer fmt...

---

*この記事は自動収集システムによって保存されました。*
