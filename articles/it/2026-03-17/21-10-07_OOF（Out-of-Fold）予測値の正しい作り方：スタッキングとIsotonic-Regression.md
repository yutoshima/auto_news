---
title: "07_OOF（Out-of-Fold）予測値の正しい作り方：スタッキングとIsotonic Regression"
source: "Qiita (Python)"
category: "it"
published: 2026-03-17T21:10:56
url: https://qiita.com/keiba_ai_rui/items/b3424122801549107b6b
---

# 07_OOF（Out-of-Fold）予測値の正しい作り方：スタッキングとIsotonic Regression

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年03月17日 21:10
- **URL**: [https://qiita.com/keiba_ai_rui/items/b3424122801549107b6b](https://qiita.com/keiba_ai_rui/items/b3424122801549107b6b)

## 概要

はじめに
LightGBMなどのモデルをスタッキング（Stacking）で組み合わせたり、Isotonic Regressionで確率を校正（キャリブレーション）したりするとき、OOF（Out-of-Fold）予測値を正しく作ることが重要です。　
間違った方法で校正すると...

---

*この記事は自動収集システムによって保存されました。*
