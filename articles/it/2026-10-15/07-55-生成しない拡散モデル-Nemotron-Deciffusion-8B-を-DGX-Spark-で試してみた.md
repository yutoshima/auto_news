---
title: "生成しない拡散モデル Nemotron Deciffusion 8B を DGX Spark で試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-15T07:55:57
url: https://dev.classmethod.jp/articles/nemotron-deciffusion-8b-decision-model-dgx-spark/
---

# 生成しない拡散モデル Nemotron Deciffusion 8B を DGX Spark で試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 07:55
- **URL**: [https://dev.classmethod.jp/articles/nemotron-deciffusion-8b-decision-model-dgx-spark/](https://dev.classmethod.jp/articles/nemotron-deciffusion-8b-decision-model-dgx-spark/)

## 概要

文章を書かず、穴埋め 1 マスで判定だけを返す拡散モデル Nemotron Deciffusion 8B を DGX Spark で動かしました。手元のルーターの 528 件を流すと zero-shot で Jev と同じ水準、1 判定 138 ms。拡散モデルの意外な使い道と、足りなかったところを書きます。

---

*この記事は自動収集システムによって保存されました。*
