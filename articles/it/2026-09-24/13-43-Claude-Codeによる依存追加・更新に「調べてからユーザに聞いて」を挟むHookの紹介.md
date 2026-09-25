---
title: "Claude Codeによる依存追加・更新に「調べてからユーザに聞いて」を挟むHookの紹介"
source: "Zenn"
category: "it"
published: 2026-09-24T13:43:25
url: https://zenn.dev/sprix_it/articles/f3ef77c1d46554
---

# Claude Codeによる依存追加・更新に「調べてからユーザに聞いて」を挟むHookの紹介

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月24日 13:43
- **URL**: [https://zenn.dev/sprix_it/articles/f3ef77c1d46554](https://zenn.dev/sprix_it/articles/f3ef77c1d46554)

## 概要

背景・目的
Claude Codeなどで開発していると、こちらから依存の追加を指示していなくても、新しいライブラリを入れて実装を進めようとすることがあります。
サプライチェーン攻撃の話も最近はよく見かけるので、何を入れるのか確認せずに任せるのは少し怖いなと思っていました。
以前の記事で書いた通り、私は実装をかなり自動で回しています。
https://zenn.dev/sprix_it/articles/db685b8fd6bffe
ただ、その中でも、外部のパッケージを追加・更新するかどうかは、自分で判断したいと思っています。
そのため、依存を追加・更新する前に、調査と人間の確認を挟む...

---

*この記事は自動収集システムによって保存されました。*
