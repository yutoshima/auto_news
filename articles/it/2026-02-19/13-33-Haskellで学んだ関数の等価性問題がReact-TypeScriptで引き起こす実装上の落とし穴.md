---
title: "Haskellで学んだ関数の等価性問題がReact/TypeScriptで引き起こす実装上の落とし穴"
source: "Qiita (React)"
category: "it"
published: 2026-02-19T13:33:36
url: https://qiita.com/watanabe-gk/items/0d5c2b5137e7a381ed04
---

# Haskellで学んだ関数の等価性問題がReact/TypeScriptで引き起こす実装上の落とし穴

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年02月19日 13:33
- **URL**: [https://qiita.com/watanabe-gk/items/0d5c2b5137e7a381ed04](https://qiita.com/watanabe-gk/items/0d5c2b5137e7a381ed04)

## 概要

はじめに
Haskellを学んでいると、「関数はEqクラスのインスタンスになれない」という概念に出会います。
-- Haskellではこれがエラーになる
ghci&gt; (\x -&gt; x + 1) == (\x -&gt; x + 1)
Error: No instance for...

---

*この記事は自動収集システムによって保存されました。*
