---
title: "Gowin FPGAの配置配線オプションを実測比較 — ビルド時間とFmaxのバランス"
source: "Zenn"
category: "it"
published: 2026-10-24T04:59:37
url: https://zenn.dev/akiyukiokayasu/articles/66be017200e64e
---

# Gowin FPGAの配置配線オプションを実測比較 — ビルド時間とFmaxのバランス

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 04:59
- **URL**: [https://zenn.dev/akiyukiokayasu/articles/66be017200e64e](https://zenn.dev/akiyukiokayasu/articles/66be017200e64e)

## 概要

はじめに
Gowin EDA の Place &amp; Route には place_option と route_option というアルゴリズム選択があります。GUI では「Place Option」「Route Option」として選べる項目です。
同じRTLでも設定を変えると、ビルド時間とFmaxが変わります。しかし、どの値が有利なのかは、公式ドキュメントだけでは分かりにくいところがあります。
Tang Primer 25K (GW5A-25A) 上の 1bit PDMオシレーター実装を例に、同じRTLで設定だけを変えてビルド時間とFmaxを実測しました。

 Place ...

---

*この記事は自動収集システムによって保存されました。*
