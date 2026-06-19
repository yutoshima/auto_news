---
title: "ReactはどうやってDOMを更新する？仮想DOMと再レンダリングの仕組み"
source: "Qiita (React)"
category: "it"
published: 2026-06-18T23:55:05
url: https://qiita.com/Nagi_5417/items/291688fd871bad1f5eb5
---

# ReactはどうやってDOMを更新する？仮想DOMと再レンダリングの仕組み

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年06月18日 23:55
- **URL**: [https://qiita.com/Nagi_5417/items/291688fd871bad1f5eb5](https://qiita.com/Nagi_5417/items/291688fd871bad1f5eb5)

## 概要

はじめに
Reactを使っていると、useStateで状態を変えるだけで画面が更新されます。document.getElementByIdのようなDOM操作を自分で書くことはほとんどありません。
では、Reactは裏側でどうやってDOMを書き換えているのでしょうか？
この...

---

*この記事は自動収集システムによって保存されました。*
