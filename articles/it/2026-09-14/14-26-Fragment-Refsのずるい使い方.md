---
title: "Fragment Refsのずるい使い方"
source: "Zenn"
category: "it"
published: 2026-09-14T14:26:13
url: https://zenn.dev/uhyo/articles/react-fragment-refs-hack
---

# Fragment Refsのずるい使い方

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月14日 14:26
- **URL**: [https://zenn.dev/uhyo/articles/react-fragment-refs-hack](https://zenn.dev/uhyo/articles/react-fragment-refs-hack)

## 概要

Fragment Refsは、React 19.3で追加された新機能のひとつで、Fragmentコンポーネントがrefをサポートするようになるというものです。
ここで得られるrefはReactが用意したFragmentInstanceオブジェクトで、addEventListenerやfocusといったいくつかのメソッドを持っています。
Fragmentは何もDOM要素を描画しない、実態のないラッパーですが、FragmentInstanceを通じてそのラッパーに対して疑似的に操作を行っているかのように振る舞います。
基本的な使い方は公式ドキュメントや他の記事に譲るとして、この記事ではちょっ...

---

*この記事は自動収集システムによって保存されました。*
