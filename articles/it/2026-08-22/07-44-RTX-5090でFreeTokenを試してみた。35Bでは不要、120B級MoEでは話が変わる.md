---
title: "RTX 5090でFreeTokenを試してみた。35Bでは不要、120B級MoEでは話が変わる"
source: "Zenn"
category: "it"
published: 2026-08-22T07:44:27
url: https://zenn.dev/holy_fox/articles/53b82eed45f956
---

# RTX 5090でFreeTokenを試してみた。35Bでは不要、120B級MoEでは話が変わる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月22日 07:44
- **URL**: [https://zenn.dev/holy_fox/articles/53b82eed45f956](https://zenn.dev/holy_fox/articles/53b82eed45f956)

## 概要

2026年8月22日時点のFreeToken 0.1.2を、RTX 5090 32GBとRAM 128GBのPCで試しました。
FreeTokenは、Mixture-of-Experts（MoE）モデルのexpertをホストRAMへ置き、必要なexpertだけをGPUへキャッシュしながら推論するサービングエンジンです。狙いはvLLMやllama.cppを単純に高速化することではなく、VRAMに収まらない巨大なMoEをコンシューマ向けGPUで実用速度で動かすことにあります。
実際に試すと、この立ち位置がかなり明確に出ました。23.5GBのOrnith 1.5ではllama.cppとvLLM...

---

*この記事は自動収集システムによって保存されました。*
