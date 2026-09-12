---
title: "OpenTelemetry eBPF Instrumentationの舞台裏

日本語訳: OpenTelemetryのeBPFインストルメンテーションの舞台裏"
source: "Zenn"
category: "it"
published: 2026-09-11T02:01:34
url: https://zenn.dev/ymotongpoo/books/go-ebpf-primer
---

# OpenTelemetry eBPF Instrumentationの舞台裏

日本語訳: OpenTelemetryのeBPFインストルメンテーションの舞台裏

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月11日 02:01
- **URL**: [https://zenn.dev/ymotongpoo/books/go-ebpf-primer](https://zenn.dev/ymotongpoo/books/go-ebpf-primer)

## 概要

Go Conference 2026の登壇「OpenTelemetry eBPF Instrumentationの舞台裏」の解説資料です。eBPFによるゼロコード計装は「言語を問わず動く」と語られますが、Goバイナリへの関数レベルの計装は他言語にない4つの難所を抱えています。なぜ難しいのかを、CPUとメモリの仕組みという初歩から積み上げて、OBIの実装コードまで手元で確かめながら読める構成にしました。

---

*この記事は自動収集システムによって保存されました。*
