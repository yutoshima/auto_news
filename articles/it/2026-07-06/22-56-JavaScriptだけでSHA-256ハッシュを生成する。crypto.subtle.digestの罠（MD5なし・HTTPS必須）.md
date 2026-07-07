---
title: "JavaScriptだけでSHA-256ハッシュを生成する。crypto.subtle.digestの罠（MD5なし・HTTPS必須）"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-06T22:56:51
url: https://qiita.com/sakutto-panda/items/42dfd652de113211d782
---

# JavaScriptだけでSHA-256ハッシュを生成する。crypto.subtle.digestの罠（MD5なし・HTTPS必須）

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月06日 22:56
- **URL**: [https://qiita.com/sakutto-panda/items/42dfd652de113211d782](https://qiita.com/sakutto-panda/items/42dfd652de113211d782)

## 概要

ファイルの整合性確認やAPI署名の検証で、手元でサッとSHA-256を計算したいことがある。ブラウザには標準で Web Crypto API（crypto.subtle）が載っているので、ライブラリを一切入れずにハッシュ生成ができる。
ぱんだツールズに作ったハッシュ値生成ツ...

---

*この記事は自動収集システムによって保存されました。*
