---
title: "（備忘録）fetchでShift_JIS／gzipを受ける"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-04-17T13:24:40
url: https://qiita.com/KAI_Mutsumi/items/195a09cfb7981dac5e38
---

# （備忘録）fetchでShift_JIS／gzipを受ける

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年04月17日 13:24
- **URL**: [https://qiita.com/KAI_Mutsumi/items/195a09cfb7981dac5e38](https://qiita.com/KAI_Mutsumi/items/195a09cfb7981dac5e38)

## 概要

fetch APIのResponse:text()メソッドはUTF-8にのみ対応しています

レスポンスは常に UTF-8 としてデコードされます
MDN Response: text() メソッド

潔いですね。しかし、入力データとしてShift_JISを扱わねばならない...

---

*この記事は自動収集システムによって保存されました。*
