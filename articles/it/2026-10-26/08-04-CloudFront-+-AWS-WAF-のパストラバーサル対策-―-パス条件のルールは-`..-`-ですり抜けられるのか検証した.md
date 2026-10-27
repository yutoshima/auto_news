---
title: "CloudFront + AWS WAF のパストラバーサル対策 ― パス条件のルールは `../` ですり抜けられるのか検証した"
source: "Qiita トレンド"
category: "it"
published: 2026-10-26T08:04:33
url: https://qiita.com/k-matsu516/items/d94caff03976fb8a30f0?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items
---

# CloudFront + AWS WAF のパストラバーサル対策 ― パス条件のルールは `../` ですり抜けられるのか検証した

## メタデータ

- **情報源**: Qiita トレンド
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 08:04
- **URL**: [https://qiita.com/k-matsu516/items/d94caff03976fb8a30f0?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items](https://qiita.com/k-matsu516/items/d94caff03976fb8a30f0?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

## 概要

はじめに
パストラバーサルとは、URL のパスに ../（1つ上の階層に戻る）を含めて、本来アクセスできない場所に到達しようとする攻撃手法です。
CloudFront + AWS WAF の構成で、こうした不正なアクセスを防ぐ方法の1つに、WAF でパスを条件に許可・拒否...

---

*この記事は自動収集システムによって保存されました。*
