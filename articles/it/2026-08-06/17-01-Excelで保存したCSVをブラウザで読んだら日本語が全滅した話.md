---
title: "Excelで保存したCSVをブラウザで読んだら日本語が全滅した話"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-06T17:01:37
url: https://qiita.com/freefreefree1222/items/7fadedf2d9a2aa486dc7
---

# Excelで保存したCSVをブラウザで読んだら日本語が全滅した話

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月06日 17:01
- **URL**: [https://qiita.com/freefreefree1222/items/7fadedf2d9a2aa486dc7](https://qiita.com/freefreefree1222/items/7fadedf2d9a2aa486dc7)

## 概要

「ブラウザだけでCSVを取り込むWebアプリ」を実装していたとき、WindowsのExcelで保存されたCSVを File.text() で読み込んだら、日本語の列名が一斉に化けてしまいました。ヘッダー名のマッチングが全部失敗するため、最初は「文字コードの処理を間違えたか」...

---

*この記事は自動収集システムによって保存されました。*
