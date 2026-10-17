---
title: "2ビット量子化のMoE「Nemotron 3.5 Bolt 74B-A9B」をDGX Sparkで動かしてみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-16T06:57:22
url: https://dev.classmethod.jp/articles/dgx-spark-nemotron-3-5-bolt-74b-a9b-first-touch/
---

# 2ビット量子化のMoE「Nemotron 3.5 Bolt 74B-A9B」をDGX Sparkで動かしてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月16日 06:57
- **URL**: [https://dev.classmethod.jp/articles/dgx-spark-nemotron-3-5-bolt-74b-a9b-first-touch/](https://dev.classmethod.jp/articles/dgx-spark-nemotron-3-5-bolt-74b-a9b-first-touch/)

## 概要

Expert の重みを 2 ビットに削り 24GB に収めた Nemotron 3.5 Bolt 74B-A9B を、公開翌日に DGX Spark の llama.cpp で動かしました。DFlash で単発 61.61 tok/s、日本語 8/9、コード 49 テスト全通過。24GB というサイズの読み方も書きます。

---

*この記事は自動収集システムによって保存されました。*
