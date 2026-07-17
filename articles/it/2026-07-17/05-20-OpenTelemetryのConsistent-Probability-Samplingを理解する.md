---
title: "OpenTelemetryのConsistent Probability Samplingを理解する"
source: "Zenn"
category: "it"
published: 2026-07-17T05:20:31
url: https://zenn.dev/ymotongpoo/articles/20260717-cps
---

# OpenTelemetryのConsistent Probability Samplingを理解する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月17日 05:20
- **URL**: [https://zenn.dev/ymotongpoo/articles/20260717-cps](https://zenn.dev/ymotongpoo/articles/20260717-cps)

## 概要

SRE NEXT 2026では「サンプリングは統計学である」というタイトルで、サンプリング率を決めるときには許容誤差から標本数を逆算する必要がある、という話をしました。

このとき、トレースの一貫したサンプリングを支える仕組みとしてConsistent Probability Samplingに触れましたが、時間の都合でその中身までは踏み込みませんでした。この記事では、その部分を掘り下げて紹介します。

 TraceIdRatioBasedの限界
分散トレースのサンプリング率を下げたいとき、OpenTelemetryでまず候補に挙がるのは TraceIdRatioBased サンプラーで...

---

*この記事は自動収集システムによって保存されました。*
