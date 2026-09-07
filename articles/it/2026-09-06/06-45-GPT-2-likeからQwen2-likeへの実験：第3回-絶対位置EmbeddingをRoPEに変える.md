---
title: "GPT-2-likeからQwen2-likeへの実験：第3回 絶対位置EmbeddingをRoPEに変える"
source: "Zenn"
category: "it"
published: 2026-09-06T06:45:34
url: https://zenn.dev/yyamamot/articles/gpt2-to-qwen2-03-rope
---

# GPT-2-likeからQwen2-likeへの実験：第3回 絶対位置EmbeddingをRoPEに変える

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月06日 06:45
- **URL**: [https://zenn.dev/yyamamot/articles/gpt2-to-qwen2-03-rope](https://zenn.dev/yyamamot/articles/gpt2-to-qwen2-03-rope)

## 概要

GPT-2-likeからQwen2-likeへの実験：第3回 絶対位置EmbeddingをRoPEに変える
GPT-2-likeからQwen2-likeへ、少しずつ構造を変更する実験の第3回です。今回は学習可能な絶対位置Embeddingを外し、RoPEへ変更します。
第2回では、GELUをSwiGLUへ変更しました。検証Lossは改善しましたが、学習は少し遅くなりました。今回は品質指標の差がさらに大きく出ています。その代わり、速度の低下もかなり明確でした。
先に結果を書くと下記です。

検証Lossと正解率は5つすべてのseedで改善した
パラメーターは32,768減った
学習時間...

---

*この記事は自動収集システムによって保存されました。*
