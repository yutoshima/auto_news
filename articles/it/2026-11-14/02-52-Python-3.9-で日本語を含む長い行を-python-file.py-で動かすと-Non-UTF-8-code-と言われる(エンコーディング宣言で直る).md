---
title: "Python 3.9 で日本語を含む長い行を python file.py で動かすと Non-UTF-8 code と言われる(エンコーディング宣言で直る)"
source: "Qiita (Python)"
category: "it"
published: 2026-11-14T02:52:35
url: https://qiita.com/takamatt_ai/items/c3cf9df22727268997da
---

# Python 3.9 で日本語を含む長い行を python file.py で動かすと Non-UTF-8 code と言われる(エンコーディング宣言で直る)

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月14日 02:52
- **URL**: [https://qiita.com/takamatt_ai/items/c3cf9df22727268997da](https://qiita.com/takamatt_ai/items/c3cf9df22727268997da)

## 概要

この記事を読み終えると、UTF-8 で保存したはずの Python ファイルが SyntaxError: Non-UTF-8 code で落ちる条件と、3つの直し方がわかります。
根拠は、手元の Windows 11 のノート(Python 3.9.13)で、小さなファイル...

---

*この記事は自動収集システムによって保存されました。*
