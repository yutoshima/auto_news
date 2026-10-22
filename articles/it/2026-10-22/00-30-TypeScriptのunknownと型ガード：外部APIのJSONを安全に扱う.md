---
title: "TypeScriptのunknownと型ガード：外部APIのJSONを安全に扱う"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-22T00:30:06
url: https://qiita.com/sponge841841/items/51eb35b227caef15de1c
---

# TypeScriptのunknownと型ガード：外部APIのJSONを安全に扱う

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 00:30
- **URL**: [https://qiita.com/sponge841841/items/51eb35b227caef15de1c](https://qiita.com/sponge841841/items/51eb35b227caef15de1c)

## 概要

fetch() で外部APIからJSONを受け取ると、つい次のように書きたくなります。
// これは「型が正しい」という実行時の保証にはならない
const user = (await response.json()) as ApiUser;
console.log(use...

---

*この記事は自動収集システムによって保存されました。*
