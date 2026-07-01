---
title: "ReactのStateを直接変更してはいけない理由と正しい更新方法"
source: "Qiita (React)"
category: "it"
published: 2026-06-30T14:35:19
url: https://qiita.com/arakink/items/e505c589ce4c2f136993
---

# ReactのStateを直接変更してはいけない理由と正しい更新方法

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年06月30日 14:35
- **URL**: [https://qiita.com/arakink/items/e505c589ce4c2f136993](https://qiita.com/arakink/items/e505c589ce4c2f136993)

## 概要

はじめに
React の State では、オブジェクトや配列を扱うときに 直接変更しない ことが重要です。
オブジェクトや配列を直接変更せず、新しいオブジェクトや新しい配列を作って更新することを、イミュータブルに扱う と言います。
たとえば、次のような State があ...

---

*この記事は自動収集システムによって保存されました。*
