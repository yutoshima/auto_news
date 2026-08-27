---
title: "Base64で日本語が壊れるのはなぜか — btoa/atobのマルチバイト問題とTextEncoderで直す"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-27T02:17:41
url: https://qiita.com/sakutto-panda/items/36d530b4b83ae1baea04
---

# Base64で日本語が壊れるのはなぜか — btoa/atobのマルチバイト問題とTextEncoderで直す

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月27日 02:17
- **URL**: [https://qiita.com/sakutto-panda/items/36d530b4b83ae1baea04](https://qiita.com/sakutto-panda/items/36d530b4b83ae1baea04)

## 概要

3行まとめ

ブラウザ標準の btoa("日本語") は例外を投げる。btoa は各文字を0〜255の1バイトとみなすバイナリ文字列専用で、UTF-16のマルチバイト文字を渡せないため
正しくは「文字列 →（TextEncoder）→ UTF-8バイト列 →（fromCh...

---

*この記事は自動収集システムによって保存されました。*
