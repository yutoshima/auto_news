---
title: "「エラー: 期待されるキー・デスクリプタが見つからず、空文字が \"\" にあります」 RTLで input type=\"number\" のデフォルト値 0 を消す"
source: "Qiita トレンド"
category: "it"
published: 2026-11-14T05:59:42
url: https://qiita.com/J-T_ky2g/items/757b73893b5fde454b83?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items
---

# 「エラー: 期待されるキー・デスクリプタが見つからず、空文字が "" にあります」 RTLで input type="number" のデフォルト値 0 を消す

## メタデータ

- **情報源**: Qiita トレンド
- **カテゴリ**: it
- **公開日時**: 2026年11月14日 05:59
- **URL**: [https://qiita.com/J-T_ky2g/items/757b73893b5fde454b83?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items](https://qiita.com/J-T_ky2g/items/757b73893b5fde454b83?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

## 概要

はじめに

input type="number"のデフォルト値0を消して未入力のバリデーションテストをしたかった

問題

値を触らないと0になり未入力でなくなる

解決

userEventを使う場合
await userEvent.clear(timeInput...

---

*この記事は自動収集システムによって保存されました。*
