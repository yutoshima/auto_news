---
title: "重いループ処理でUIを止めないために MessageChannel で yield する"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-03T17:30:30
url: https://qiita.com/kiyuka/items/4dff7b562432d45f0136
---

# 重いループ処理でUIを止めないために MessageChannel で yield する

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月03日 17:30
- **URL**: [https://qiita.com/kiyuka/items/4dff7b562432d45f0136](https://qiita.com/kiyuka/items/4dff7b562432d45f0136)

## 概要

はじめに
JavaScriptで他の処理を邪魔しないように重いループ処理を実行したーい！

結論
できました！
// 重い処理のループ
async function processItems(items: Item[]) {
  for (const [i, item] ...

---

*この記事は自動収集システムによって保存されました。*
