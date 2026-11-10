---
title: "DGX Sparkを2台でLLM生成を1.8倍速化、llama.cppがNCCLに対応"
source: "PC Watch"
category: "it"
published: 2026-11-09T07:13:06
url: https://pc.watch.impress.co.jp/docs/news/2154660.html
---

# DGX Sparkを2台でLLM生成を1.8倍速化、llama.cppがNCCLに対応

## メタデータ

- **情報源**: PC Watch
- **カテゴリ**: it
- **公開日時**: 2026年11月09日 07:13
- **URL**: [https://pc.watch.impress.co.jp/docs/news/2154660.html](https://pc.watch.impress.co.jp/docs/news/2154660.html)

## 概要

NVIDIAのAIミニPC「DGX Spark」を2台つなぐと、LLMの推論速度が1台の最大約1.8倍になる。ggml-orgは11月4日(米国時間)、ローカルLLM推論エンジン「llama.cpp v0.9.0」を公開した。このバージョンでは、内部で使用するテンソル演算ライブラリ「ggml」をv0.29.0に更新した。これにより、複数台のマシンでテンソル並列推論を行なう際の通信に、NVIDIAの通信ライブラリ「NCCL」を使用できるようになった。

---

*この記事は自動収集システムによって保存されました。*
