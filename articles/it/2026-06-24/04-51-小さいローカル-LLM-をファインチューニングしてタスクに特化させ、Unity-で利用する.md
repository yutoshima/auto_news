---
title: "小さいローカル LLM をファインチューニングしてタスクに特化させ、Unity で利用する"
source: "Zenn"
category: "it"
published: 2026-06-24T04:51:06
url: https://zenn.dev/meson_tech_blog/articles/fine-tuning-local-llm
---

# 小さいローカル LLM をファインチューニングしてタスクに特化させ、Unity で利用する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月24日 04:51
- **URL**: [https://zenn.dev/meson_tech_blog/articles/fine-tuning-local-llm](https://zenn.dev/meson_tech_blog/articles/fine-tuning-local-llm)

## 概要

はじめに
以下の記事を読んで、自分でもローカル LLM をファインチューニングしてみよう、と思ってやってみたことをまとめた記事です。
加えて、せっかくなので Unity で扱える形までやってみたのでそれについても書こうと思います。
https://zenn.dev/sompojapan_dx/articles/74624afa03040c
今回の記事では MLX を用いてファインチューニングします。対象のモデルは mlx-community/gemma-3n-E2B-it-lm-4bit です。
また、モデル全体を更新するのではなく、LoRA（Low-Rank Adaptation...

---

*この記事は自動収集システムによって保存されました。*
