---
title: "Vitestでモックをテストケースごとに差し替えた値が残る"
source: "Qiita トレンド"
category: "it"
published: 2026-11-07T22:25:04
url: https://qiita.com/J-T_ky2g/items/fc1d307ea464e734af9e?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items
---

# Vitestでモックをテストケースごとに差し替えた値が残る

## メタデータ

- **情報源**: Qiita トレンド
- **カテゴリ**: it
- **公開日時**: 2026年11月07日 22:25
- **URL**: [https://qiita.com/J-T_ky2g/items/fc1d307ea464e734af9e?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items](https://qiita.com/J-T_ky2g/items/fc1d307ea464e734af9e?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

## 概要

はじめに
以下の後に次のテストを書いてうまくいかなかった

問題

「学習履歴が表示される」でモックが残ってうまくいかない

const { useGetLearnRecords } = vi.hoisted(() =&gt; {
  return {
    useGe...

---

*この記事は自動収集システムによって保存されました。*
