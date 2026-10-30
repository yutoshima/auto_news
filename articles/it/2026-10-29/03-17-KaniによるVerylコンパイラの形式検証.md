---
title: "KaniによるVerylコンパイラの形式検証"
source: "Zenn"
category: "it"
published: 2026-10-29T03:17:06
url: https://zenn.dev/dalance/articles/44a8f80ea0cfa1
---

# KaniによるVerylコンパイラの形式検証

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月29日 03:17
- **URL**: [https://zenn.dev/dalance/articles/44a8f80ea0cfa1](https://zenn.dev/dalance/articles/44a8f80ea0cfa1)

## 概要

はじめに
現在開発中のハードウェア記述言語Verylではコンパイラ中に様々な式評価があります。
この式評価においては、例えば各ビットは0/1の2値ではなく0/1/x/zの4値だったり、変数のサイズは可変（1ビットから数千ビットまで）だったりと、単純な固定長整数型の四則演算に比べてかなり複雑です。
さらに、VerylはSystemVerilogの意味論を継承しているため、SystemVerilogの規格書（IEEE 1800-2023）に書かれた細かい式評価のルールにも準拠する必要があります。
また、Verylコンパイラが内蔵しているRTLシミュレータでは高速化のためにCranelif...

---

*この記事は自動収集システムによって保存されました。*
