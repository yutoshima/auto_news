---
title: "一階述語論理の代入をPythonで実装する：全称閉包と変数捕獲を避ける置換"
source: "Qiita (Python)"
category: "it"
published: 2026-07-30T17:54:07
url: https://qiita.com/skrtk98/items/7a4ed9c3e902a897e6bf
---

# 一階述語論理の代入をPythonで実装する：全称閉包と変数捕獲を避ける置換

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年07月30日 17:54
- **URL**: [https://qiita.com/skrtk98/items/7a4ed9c3e902a897e6bf](https://qiita.com/skrtk98/items/7a4ed9c3e902a897e6bf)

## 概要

前の記事：一階述語論理をPythonで組み立てる：論理式の構文木と自由変数
一階述語論理では、論理式の中に現れる変数へ項を代入します。例えば、$P(x)$ に $y$ を代入すると $P(y)$ になります。
しかし、量化記号を含む式では、単純な文字列置換は使えません。置換...

---

*この記事は自動収集システムによって保存されました。*
