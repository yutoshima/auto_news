---
title: "文字コードの自動判定はどう動くか — BOMとバイトパターンスコアリングでUTF-8/Shift_JIS/EUC-JPを見分ける"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-27T22:46:05
url: https://qiita.com/sakutto-panda/items/8ab3f4252233141d84b0
---

# 文字コードの自動判定はどう動くか — BOMとバイトパターンスコアリングでUTF-8/Shift_JIS/EUC-JPを見分ける

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月27日 22:46
- **URL**: [https://qiita.com/sakutto-panda/items/8ab3f4252233141d84b0](https://qiita.com/sakutto-panda/items/8ab3f4252233141d84b0)

## 概要

3行まとめ

テキストファイルの文字コード（UTF-8 / Shift_JIS / EUC-JP / UTF-16）をブラウザ内で自動判定するツールを作った。ライブラリ不使用、Uint8Array の走査だけで実装している
ブラウザの TextDecoder は「指定した...

---

*この記事は自動収集システムによって保存されました。*
