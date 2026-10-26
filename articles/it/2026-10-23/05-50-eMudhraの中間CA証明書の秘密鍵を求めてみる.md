---
title: "eMudhraの中間CA証明書の秘密鍵を求めてみる"
source: "Zenn"
category: "it"
published: 2026-10-23T05:50:11
url: https://zenn.dev/herumi/articles/search_bad_emudhra_key
---

# eMudhraの中間CA証明書の秘密鍵を求めてみる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 05:50
- **URL**: [https://zenn.dev/herumi/articles/search_bad_emudhra_key](https://zenn.dev/herumi/articles/search_bad_emudhra_key)

## 概要

はじめに
2026年10月に認証局eMudhraの中間CA証明書の署名鍵（秘密鍵）が脆弱だったという報告がありました。
ここではそのCA証明書に記載された検証鍵（公開鍵）から署名鍵を実際に求めてみます。

 Pythonを使って求める
脆弱だった秘密鍵は8ビット以下だったということで、洗練された高速なライブラリを使わずナイーブな方法を使います。
『Software Design 2022年3月号』で紹介した記事、楕円曲線暗号のPythonによる実装その1（有限体とECDH鍵共有）で使った楕円曲線の点の演算コードを利用しましょう。
ソースコードはsrc/eccに置きました。
これらは有...

---

*この記事は自動収集システムによって保存されました。*
