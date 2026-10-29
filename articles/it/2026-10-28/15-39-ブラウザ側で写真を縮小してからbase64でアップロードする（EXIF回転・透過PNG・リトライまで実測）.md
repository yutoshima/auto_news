---
title: "ブラウザ側で写真を縮小してからbase64でアップロードする（EXIF回転・透過PNG・リトライまで実測）"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-28T15:39:41
url: https://qiita.com/alanplusplus/items/ce5ab57b8a8550870042
---

# ブラウザ側で写真を縮小してからbase64でアップロードする（EXIF回転・透過PNG・リトライまで実測）

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 15:39
- **URL**: [https://qiita.com/alanplusplus/items/ce5ab57b8a8550870042](https://qiita.com/alanplusplus/items/ce5ab57b8a8550870042)

## 概要

個人で開発している Web アプリ Belle AI では、ユーザーが選んだ写真をブラウザ側で base64 にして、JSON で API に送っています。スマホで撮った原画像は数 MB あり、base64 にすると文字列の長さは元のバイト数の約 4/3 倍になります。モバ...

---

*この記事は自動収集システムによって保存されました。*
