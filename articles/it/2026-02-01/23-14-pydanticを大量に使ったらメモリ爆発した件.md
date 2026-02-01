---
title: "pydanticを大量に使ったらメモリ爆発した件"
source: "Qiita (Python)"
category: "it"
published: 2026-02-01T23:14:56
url: https://qiita.com/kuru-to/items/03088ff74f67c1013e7b
---

# pydanticを大量に使ったらメモリ爆発した件

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年02月01日 23:14
- **URL**: [https://qiita.com/kuru-to/items/03088ff74f67c1013e7b](https://qiita.com/kuru-to/items/03088ff74f67c1013e7b)

## 概要

概要
pydantic.BaseModel を継承したクラスのインスタンスを大量に生成した結果, メモリ上限を突破する問題が発生した. オブジェクト数の推移を確認したところ, set や dict といった一般的なオブジェクトが数十万単位で生成されており, 具体的にどのオ...

---

*この記事は自動収集システムによって保存されました。*
