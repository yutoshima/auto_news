---
title: "【React】リスト内の各子要素には固有の「key」propが必要です。これが問題ないはずなのに。"
source: "Qiita (React)"
category: "it"
published: 2026-09-21T08:35:08
url: https://qiita.com/J-T_ky2g/items/30e27e5543f164c27c2f
---

# 【React】リスト内の各子要素には固有の「key」propが必要です。これが問題ないはずなのに。

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年09月21日 08:35
- **URL**: [https://qiita.com/J-T_ky2g/items/30e27e5543f164c27c2f](https://qiita.com/J-T_ky2g/items/30e27e5543f164c27c2f)

## 概要

はじめに

apiからデータフェッチして既存処理のinitialStateに登録していた

問題

キーとして使っているプロパティも問題なく存在するデータなのに、表題のエラーが出る

解決

initialStateとして使用するArrayのデータが、 const [...

---

*この記事は自動収集システムによって保存されました。*
