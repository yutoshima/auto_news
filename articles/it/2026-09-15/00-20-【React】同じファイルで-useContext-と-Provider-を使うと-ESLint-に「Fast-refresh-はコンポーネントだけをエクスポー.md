---
title: "【React】同じファイルで useContext と Provider を使うと ESLint に「Fast refresh はコンポーネントだけをエクスポートするファイルでのみ機能します。React コンテキストを別ファイルへ移動してください (react-refresh/only-export-components)」と表示されます"
source: "Qiita (React)"
category: "it"
published: 2026-09-15T00:20:45
url: https://qiita.com/J-T_ky2g/items/15c9da7dc118e2e6cb8c
---

# 【React】同じファイルで useContext と Provider を使うと ESLint に「Fast refresh はコンポーネントだけをエクスポートするファイルでのみ機能します。React コンテキストを別ファイルへ移動してください (react-refresh/only-export-components)」と表示されます

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年09月15日 00:20
- **URL**: [https://qiita.com/J-T_ky2g/items/15c9da7dc118e2e6cb8c](https://qiita.com/J-T_ky2g/items/15c9da7dc118e2e6cb8c)

## 概要

はじめに

eslintのエラーに対する対応

問題

eslintの警告が出ている。実際に何が問題になるのかまでは調べられていない

解決

ファイルを分けたらeslintエラーは出なくなった

終わりに

実際にどういったデメリットがあるのか実験したい

---

*この記事は自動収集システムによって保存されました。*
