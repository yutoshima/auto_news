---
title: "同じRust製のBiomeとOxlintで、なぜ速度差が大きいのか"
source: "Zenn"
category: "it"
published: 2026-08-13T03:00:09
url: https://zenn.dev/estie/articles/64b80da2fbf175
---

# 同じRust製のBiomeとOxlintで、なぜ速度差が大きいのか

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月13日 03:00
- **URL**: [https://zenn.dev/estie/articles/64b80da2fbf175](https://zenn.dev/estie/articles/64b80da2fbf175)

## 概要

はじめに
こんにちは、デザインエンジニアのyamarinです。
BiomeとOxlintは、同じRust製でどちらも速い印象がありますね。
estie(エスティ)ではfrontendの静的解析ツールにBiomeを採用しており、Oxlintどんなもんかなと大体同じ条件で試してみたところ、条件次第でOxlintの方が約4.9倍速い結果となりました。
同じRustなのになぜ差が出るのか気になったので、調べてみました！

 実測: 負荷を揃えて測る
私の担当プロダクト（TS/TSX約800ファイル）で測った結果がこちらです。



計測条件
Biome 2.5.3
Oxlint 1.77
差...

---

*この記事は自動収集システムによって保存されました。*
