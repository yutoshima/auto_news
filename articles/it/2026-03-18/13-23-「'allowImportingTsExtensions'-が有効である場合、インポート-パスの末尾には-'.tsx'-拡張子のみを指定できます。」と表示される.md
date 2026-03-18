---
title: "「'allowImportingTsExtensions' が有効である場合、インポート パスの末尾には '.tsx' 拡張子のみを指定できます。」と表示される件"
source: "Qiita (React)"
category: "it"
published: 2026-03-18T13:23:03
url: https://qiita.com/o68606007/items/07bd06ea4a5f842386a9
---

# 「'allowImportingTsExtensions' が有効である場合、インポート パスの末尾には '.tsx' 拡張子のみを指定できます。」と表示される件

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年03月18日 13:23
- **URL**: [https://qiita.com/o68606007/items/07bd06ea4a5f842386a9](https://qiita.com/o68606007/items/07bd06ea4a5f842386a9)

## 概要

はじめに
CI/CDを用いてテストを実行する際に、上記のエラーが出力されていました。

問題

main
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
...

---

*この記事は自動収集システムによって保存されました。*
