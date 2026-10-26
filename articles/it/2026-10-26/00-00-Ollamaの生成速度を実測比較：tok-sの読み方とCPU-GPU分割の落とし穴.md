---
title: "Ollamaの生成速度を実測比較：tok/sの読み方とCPU/GPU分割の落とし穴"
source: "Qiita (Python)"
category: "it"
published: 2026-10-26T00:00:04
url: https://qiita.com/warrobotsxyz/items/e4833747d780886e1d8b
---

# Ollamaの生成速度を実測比較：tok/sの読み方とCPU/GPU分割の落とし穴

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 00:00
- **URL**: [https://qiita.com/warrobotsxyz/items/e4833747d780886e1d8b](https://qiita.com/warrobotsxyz/items/e4833747d780886e1d8b)

## 概要

はじめに
「8Bクラスのモデルをローカルで動かすと遅い」——その遅さは、実は設定次第で3倍以上変わります。本記事では /api/generate のレスポンスに含まれる計測値で生成速度（tok/s）を正しく測り、同じ qwen3:8b が 9.1 tok/s → 33.3...

---

*この記事は自動収集システムによって保存されました。*
