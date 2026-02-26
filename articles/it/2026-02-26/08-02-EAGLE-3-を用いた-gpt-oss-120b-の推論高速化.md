---
title: "EAGLE-3 を用いた gpt-oss-120b の推論高速化"
source: "Zenn"
category: "it"
published: 2026-02-26T08:02:18
url: https://zenn.dev/fixstars/articles/eagle3_gptoss120b
---

# EAGLE-3 を用いた gpt-oss-120b の推論高速化

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月26日 08:02
- **URL**: [https://zenn.dev/fixstars/articles/eagle3_gptoss120b](https://zenn.dev/fixstars/articles/eagle3_gptoss120b)

## 概要

概要
LLM を高速に推論する手法の一つに投機的デコード (Speculative Decoding) があります。この記事では、OpenAI 社のオープンウェイト LLM gpt-oss-120b を題材として、投機的デコード手法のひとつである EAGLE-3 を使うことによる実行時間の変化を NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition で測定し、どのような場合に EAGLE-3 を使うのが適切かについて検討しました。

 手法
まず、今回の記事で利用する手法について簡単に説明します。

 投機的デコード
http...

---

*この記事は自動収集システムによって保存されました。*
