---
title: "RustでFiberを用いたJob Systemを実装したらReleaseビルドでバグが発生した"
source: "Zenn"
category: "it"
published: 2026-11-25T10:24:41
url: https://zenn.dev/otinpan/articles/082f6178eb1472
---

# RustでFiberを用いたJob Systemを実装したらReleaseビルドでバグが発生した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 10:24
- **URL**: [https://zenn.dev/otinpan/articles/082f6178eb1472](https://zenn.dev/otinpan/articles/082f6178eb1472)

## 概要

はじめに
現在、RustとVulkanを用いた自作ゲームエンジン KaniVolcanoEngine を開発しています。
KaniVolcanoEngineでは、Jobの並列実行を実現するために、WindowsのFiber APIを用いたJob Systemを実装しています。
今回、ReleaseビルドでJob Systemを動作させたところ、assertによるpanicや、RefCellの借用エラーが発生しました。原因を調査する過程で、Fiberのスレッド間移動と、コンパイラによるTLS（Thread Local Storage）アクセスの最適化が関係している可能性が浮上しました。...

---

*この記事は自動収集システムによって保存されました。*
