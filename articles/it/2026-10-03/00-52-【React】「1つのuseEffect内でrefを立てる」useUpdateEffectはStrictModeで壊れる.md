---
title: "【React】「1つのuseEffect内でrefを立てる」useUpdateEffectはStrictModeで壊れる"
source: "Qiita (React)"
category: "it"
published: 2026-10-03T00:52:32
url: https://qiita.com/shun123/items/b7a01b3d7379274d3ebc
---

# 【React】「1つのuseEffect内でrefを立てる」useUpdateEffectはStrictModeで壊れる

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年10月03日 00:52
- **URL**: [https://qiita.com/shun123/items/b7a01b3d7379274d3ebc](https://qiita.com/shun123/items/b7a01b3d7379274d3ebc)

## 概要

はじめに
「初回マウント時は実行せず、依存配列が変わったときだけ実行したい」という場面で、useUpdateEffect のようなカスタムフックを自作することがあります。
ネットでよく見かける実装は「1つの useEffect の中で ref を立てる」形ですが、この実装...

---

*この記事は自動収集システムによって保存されました。*
