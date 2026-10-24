---
title: "eMudhraの中間CA証明書の秘密鍵を求めてみる"
source: "はてブ テクノロジー"
category: "it"
published: 2026-10-23T08:32:23
url: https://zenn.dev/herumi/articles/search_bad_emudhra_key
---

# eMudhraの中間CA証明書の秘密鍵を求めてみる

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 08:32
- **URL**: [https://zenn.dev/herumi/articles/search_bad_emudhra_key](https://zenn.dev/herumi/articles/search_bad_emudhra_key)

## 概要

はじめに 2026年10月に認証局eMudhraの中間CA証明書の署名鍵（秘密鍵）が脆弱だったという報告がありました。 ここではそのCA証明書に記載された検証鍵（公開鍵）から署名鍵を実際に求めてみます。 Pythonを使って求める 脆弱だった秘密鍵は8ビット以下だったということで、洗練された高速なライブラリを使わずナイーブ...

---

*この記事は自動収集システムによって保存されました。*
