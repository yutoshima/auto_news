---
title: "JavaScript: base64高速化（2）"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-18T21:59:16
url: https://qiita.com/mashuel/items/eb65e95a7cf74e6cd8fd
---

# JavaScript: base64高速化（2）

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月18日 21:59
- **URL**: [https://qiita.com/mashuel/items/eb65e95a7cf74e6cd8fd](https://qiita.com/mashuel/items/eb65e95a7cf74e6cd8fd)

## 概要

base64符号化/復号の高速化の続編。以下の4種類で試しやがっときました。果たして更なる高速化を達成できるのか?

入出力ともにTypedArray利用
入力はDataView、出力はTypedArray利用
入力はTypedArray、出力はDataView利用
入出力...

---

*この記事は自動収集システムによって保存されました。*
