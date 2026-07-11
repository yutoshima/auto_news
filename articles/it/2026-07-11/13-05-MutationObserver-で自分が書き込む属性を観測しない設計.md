---
title: "MutationObserver で自分が書き込む属性を観測しない設計"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-11T13:05:05
url: https://qiita.com/mori-dev@github/items/9b3d8a73fe0e5c81ad85
---

# MutationObserver で自分が書き込む属性を観測しない設計

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月11日 13:05
- **URL**: [https://qiita.com/mori-dev@github/items/9b3d8a73fe0e5c81ad85](https://qiita.com/mori-dev@github/items/9b3d8a73fe0e5c81ad85)

## 概要

SPAでは、初回表示後にもJavaScriptによってDOM要素が追加されます。後から追加された画像にloading="lazy"を設定するようなスクリプトでは、MutationObserverを使ってDOMの変化を監視できます。
一方、処理済みの要素を判別するために独自属...

---

*この記事は自動収集システムによって保存されました。*
