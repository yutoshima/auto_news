---
title: "Ternary Bonsai 2 27BをM1 Pro・16GBで動かす"
source: "Zenn"
category: "it"
published: 2026-09-19T15:05:52
url: https://zenn.dev/okame_rara/articles/bonsai_2_27b_m1
---

# Ternary Bonsai 2 27BをM1 Pro・16GBで動かす

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月19日 15:05
- **URL**: [https://zenn.dev/okame_rara/articles/bonsai_2_27b_m1](https://zenn.dev/okame_rara/articles/bonsai_2_27b_m1)

## 概要

こんにちは、はたけです。
今回はM1 Pro・メモリ16GBのMacBook Proで、Ternary Bonsai 2 27Bを動かしてみました。PrismML公式のllama.cpp forkをソースからビルドし、日本語の応答が返るところまで確認できました。
短い動作確認では 8.1 tokens/s、その後の対話形式での自己紹介では 9.6 tokens/s と表示されました。本格的なベンチマークではありませんが、手元のMacで27Bクラスのモデルを動かせたのはうれしいですね。
ただ、環境構築はなかなかめんどくさい。
なので、この記事ではPrismML公式のllama.cpp fo...

---

*この記事は自動収集システムによって保存されました。*
