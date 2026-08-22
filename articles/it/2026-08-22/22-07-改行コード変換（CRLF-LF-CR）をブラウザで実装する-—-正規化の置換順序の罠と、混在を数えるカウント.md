---
title: "改行コード変換（CRLF/LF/CR）をブラウザで実装する — 正規化の置換順序の罠と、混在を数えるカウント"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-22T22:07:34
url: https://qiita.com/sakutto-panda/items/d1dbdf0b404ac36f1619
---

# 改行コード変換（CRLF/LF/CR）をブラウザで実装する — 正規化の置換順序の罠と、混在を数えるカウント

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月22日 22:07
- **URL**: [https://qiita.com/sakutto-panda/items/d1dbdf0b404ac36f1619](https://qiita.com/sakutto-panda/items/d1dbdf0b404ac36f1619)

## 概要

3行まとめ

CRLF・LF・CR を相互変換するブラウザ完結ツールを作った。肝は「一度LFに正規化してから目的の改行コードへ変換する」2段構え
正規化の置換は \r\n → \n を先、\r → \n を後にやる。順序を逆にすると \r\n が \n\n になって空行が...

---

*この記事は自動収集システムによって保存されました。*
