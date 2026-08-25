---
title: "状態空間モデルにおけるFilteringとSmoothingの違いを理解する"
source: "Zenn"
category: "it"
published: 2026-08-25T02:04:16
url: https://zenn.dev/ca_kagglers/articles/ssm-filtering-smoothing
---

# 状態空間モデルにおけるFilteringとSmoothingの違いを理解する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月25日 02:04
- **URL**: [https://zenn.dev/ca_kagglers/articles/ssm-filtering-smoothing](https://zenn.dev/ca_kagglers/articles/ssm-filtering-smoothing)

## 概要

はじめに
ihiratchです。本記事では、状態空間モデルにおけるFiltering（フィルタリング）とSmoothing（平滑化）の違いを整理します。
状態空間モデルでは、時系列の観測データをもとに、直接観測できない状態を推定します。その代表的な方法がFilteringとSmoothingです。最近参加したKaggleのROGII - Wellbore Geology Predictionで両方の手法を使う機会がありましたが、両者の違いを十分に整理できていなかったため、この機会にあらためて学び直すことにしました。
ざっくりいうと、Filteringは過去から現在までの観測から現在の...

---

*この記事は自動収集システムによって保存されました。*
