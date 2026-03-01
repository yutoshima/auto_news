---
title: "テスト不足でデグレ11回。Double-Loop TDDで「書いたコードが壊れない」仕組みを作る ― Python・TypeScript・Go実装比較"
source: "Qiita (Python)"
category: "it"
published: 2026-03-01T22:07:19
url: https://qiita.com/nrEngineer/items/41a36efa83c245d93b1d
---

# テスト不足でデグレ11回。Double-Loop TDDで「書いたコードが壊れない」仕組みを作る ― Python・TypeScript・Go実装比較

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年03月01日 22:07
- **URL**: [https://qiita.com/nrEngineer/items/41a36efa83c245d93b1d](https://qiita.com/nrEngineer/items/41a36efa83c245d93b1d)

## 概要

TL;DR

AIにリファクタリングを任せると依存先が静かに壊れる（11件のデグレ経験）
3パターンに集約: API修正→呼び出し元破壊、共通コンポーネント変更→画面崩壊、DB変更→データ不整合

Canon TDD（Kent Beck 2023）: Red→Green→...

---

*この記事は自動収集システムによって保存されました。*
