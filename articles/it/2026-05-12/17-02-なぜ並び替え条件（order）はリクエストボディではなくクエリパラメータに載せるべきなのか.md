---
title: "なぜ並び替え条件（order）はリクエストボディではなくクエリパラメータに載せるべきなのか"
source: "Qiita (React)"
category: "it"
published: 2026-05-12T17:02:27
url: https://qiita.com/watanabe_trtr/items/b3a84d6df2960ed887ce
---

# なぜ並び替え条件（order）はリクエストボディではなくクエリパラメータに載せるべきなのか

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年05月12日 17:02
- **URL**: [https://qiita.com/watanabe_trtr/items/b3a84d6df2960ed887ce](https://qiita.com/watanabe_trtr/items/b3a84d6df2960ed887ce)

## 概要

はじめに
APIを設計する際、ソート順を指定する order や sort といったパラメータをどこに配置するか迷うことがあります。
「POSTメソッドでボディに入れれば、複雑な条件も送りやすいのでは？」と考える方もいるかもしれませんが、Web APIの標準的な設計（特に...

---

*この記事は自動収集システムによって保存されました。*
