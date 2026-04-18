---
title: "Async React時代の宣言的UI 2: トランジション対応のuseDebouncedフックを作る"
source: "Zenn"
category: "it"
published: 2026-04-18T08:54:05
url: https://zenn.dev/uhyo/articles/async-react-debounce-2
---

# Async React時代の宣言的UI 2: トランジション対応のuseDebouncedフックを作る

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月18日 08:54
- **URL**: [https://zenn.dev/uhyo/articles/async-react-debounce-2](https://zenn.dev/uhyo/articles/async-react-debounce-2)

## 概要

皆さんこんにちは。以下の記事では、Async React時代の宣言的UIとして、デバウンスをuseDeferredValueで代替する方法を示しました。
https://zenn.dev/uhyo/articles/async-react-debounce
記事の末尾で「実際には、ネットワークアクセスをデバウンスしている場合とか応用形もあるのですが」と述べたので、今回はネットワークアクセスを含む場合について考えたいと思います。
今回の記事に登場するコードは以下のStackBlitzで実際に動作を確認できます。


 今回の要件
前回の記事では、ユーザーが入力すると、フロントエンドで検索結...

---

*この記事は自動収集システムによって保存されました。*
