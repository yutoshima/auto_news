---
title: "JSONの差分を「テキスト」でなく「構造」で取る——JavaScriptの再帰で書くJSON diffとキー順・配列の罠"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-02T22:53:16
url: https://qiita.com/sakutto-panda/items/d6b1ebb98f26068d90d8
---

# JSONの差分を「テキスト」でなく「構造」で取る——JavaScriptの再帰で書くJSON diffとキー順・配列の罠

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月02日 22:53
- **URL**: [https://qiita.com/sakutto-panda/items/d6b1ebb98f26068d90d8](https://qiita.com/sakutto-panda/items/d6b1ebb98f26068d90d8)

## 概要

API レスポンスの新旧を比べたいとき、テキスト差分ツールに貼ると地獄を見る。インデントが違う・キーの順番が違う・改行位置が違う、それだけで全行が「差分あり」になる。本当に知りたいのは「どのキーが増えて、どの値が変わったか」という構造の差分なのに。
JSON を構造レベルで...

---

*この記事は自動収集システムによって保存されました。*
