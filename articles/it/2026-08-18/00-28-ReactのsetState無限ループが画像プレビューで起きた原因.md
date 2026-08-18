---
title: "ReactのsetState無限ループが画像プレビューで起きた原因"
source: "Qiita (React)"
category: "it"
published: 2026-08-18T00:28:01
url: https://qiita.com/hiro123/items/1c40c9e35d4058ee75fb
---

# ReactのsetState無限ループが画像プレビューで起きた原因

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年08月18日 00:28
- **URL**: [https://qiita.com/hiro123/items/1c40c9e35d4058ee75fb](https://qiita.com/hiro123/items/1c40c9e35d4058ee75fb)

## 概要

ピクセル画像のプレビューでMaximum update depth exceededが発生しました。useEffectの依存配列ではなく、キャッシュ済み画像を補完するref callbackとonLoad内のsetStateが循環していました。

起きていた循環
画像の自然...

---

*この記事は自動収集システムによって保存されました。*
