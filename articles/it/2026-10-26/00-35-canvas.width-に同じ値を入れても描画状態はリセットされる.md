---
title: "canvas.width に同じ値を入れても描画状態はリセットされる"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-26T00:35:15
url: https://qiita.com/morphio/items/9c036a33838c065a1e9e
---

# canvas.width に同じ値を入れても描画状態はリセットされる

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 00:35
- **URL**: [https://qiita.com/morphio/items/9c036a33838c065a1e9e](https://qiita.com/morphio/items/9c036a33838c065a1e9e)

## 概要

canvas.width に現在と同じ値を代入しても、描画バッファとコンテキストの状態はリセットされる。幅を揃えるための代入でも、すでに描いた内容は消える。
サイズを決めてから fillStyle や変換を設定する。幅への代入で、それらも初期状態へ戻るためだ。CSS の表示...

---

*この記事は自動収集システムによって保存されました。*
