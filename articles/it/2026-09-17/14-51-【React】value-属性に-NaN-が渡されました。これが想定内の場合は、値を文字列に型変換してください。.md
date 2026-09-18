---
title: "【React】value 属性に NaN が渡されました。これが想定内の場合は、値を文字列に型変換してください。"
source: "Qiita (React)"
category: "it"
published: 2026-09-17T14:51:19
url: https://qiita.com/J-T_ky2g/items/fe0ea4c41b42e6c0e8d7
---

# 【React】value 属性に NaN が渡されました。これが想定内の場合は、値を文字列に型変換してください。

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年09月17日 14:51
- **URL**: [https://qiita.com/J-T_ky2g/items/fe0ea4c41b42e6c0e8d7](https://qiita.com/J-T_ky2g/items/fe0ea4c41b42e6c0e8d7)

## 概要

はじめに

これ関連

問題

以下の処理で "" に対して valueAsNumber をするため、NaN になりエラー

// console.log(e) で e > target > value の値を確認
const onChangeTime = (e) => {
  ...

---

*この記事は自動収集システムによって保存されました。*
