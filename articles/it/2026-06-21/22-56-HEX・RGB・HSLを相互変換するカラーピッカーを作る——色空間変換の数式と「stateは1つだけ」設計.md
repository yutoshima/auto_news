---
title: "HEX・RGB・HSLを相互変換するカラーピッカーを作る——色空間変換の数式と「stateは1つだけ」設計"
source: "Qiita (React)"
category: "it"
published: 2026-06-21T22:56:16
url: https://qiita.com/sakutto-panda/items/dd4f0fe1134ec267652d
---

# HEX・RGB・HSLを相互変換するカラーピッカーを作る——色空間変換の数式と「stateは1つだけ」設計

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年06月21日 22:56
- **URL**: [https://qiita.com/sakutto-panda/items/dd4f0fe1134ec267652d](https://qiita.com/sakutto-panda/items/dd4f0fe1134ec267652d)

## 概要

Figma で作った色を CSS に持っていくとき、HEX で欲しいのか rgb() なのか hsl() なのかは場面による。3形式を相互変換できるカラーピッカーは定番ツールだが、自分で作ると「色空間変換の数式」と「3つの入力をどう同期させるか」という2つの地味な課題が出て...

---

*この記事は自動収集システムによって保存されました。*
