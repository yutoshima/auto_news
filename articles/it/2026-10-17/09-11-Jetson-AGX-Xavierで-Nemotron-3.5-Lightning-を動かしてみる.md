---
title: "Jetson AGX Xavierで Nemotron 3.5 Lightning を動かしてみる"
source: "Zenn"
category: "it"
published: 2026-10-17T09:11:27
url: https://zenn.dev/nooop/articles/9d5f19aed77e18
---

# Jetson AGX Xavierで Nemotron 3.5 Lightning を動かしてみる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 09:11
- **URL**: [https://zenn.dev/nooop/articles/9d5f19aed77e18](https://zenn.dev/nooop/articles/9d5f19aed77e18)

## 概要

目的
前回、Jetson AGX XavierでQwen3.8-27Bを動かしてみましたが、5〜6 tokens/secと常用には厳しい速度でした。
https://zenn.dev/nooop/articles/f9dbdd970d3dfa
その記事のコメントで、Nemotron 3.5 Lightningなら同じくらいの賢さでもっと速く生成できるのでは、という話をいただきました。
そこで、8月にNVIDIAから公開されていたNemotron 3.5 Lightningを試してみます。
https://huggingface.co/unsloth/NVIDIA-Nemotron-3...

---

*この記事は自動収集システムによって保存されました。*
