---
title: "vLLM の /v1/decisions は同じ質問に同じ確率を返すか NVIDIA DGX Spark で確かめてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-26T02:36:30
url: https://dev.classmethod.jp/articles/dgx-spark-vllm-decisions-first-touch/
---

# vLLM の /v1/decisions は同じ質問に同じ確率を返すか NVIDIA DGX Spark で確かめてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月26日 02:36
- **URL**: [https://dev.classmethod.jp/articles/dgx-spark-vllm-decisions-first-touch/](https://dev.classmethod.jp/articles/dgx-spark-vllm-decisions-first-touch/)

## 概要

vLLM 0.33.0 に入った OpenAI 互換の /v1/decisions を DGX Spark と Qwen3-0.6B で試しました。同じ質問を 30 回ずつ送ると、答えが半々に近い質問では、他のリクエストが同時に流れている条件で、30 回の判定が 15 回ずつに割れました。

---

*この記事は自動収集システムによって保存されました。*
