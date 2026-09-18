---
title: "気軽にDGX Sparkでapt upgradeしたら壊れた話"
source: "Zenn"
category: "it"
published: 2026-09-17T07:19:25
url: https://zenn.dev/alpha_omega/articles/3f3ea4d14a0234
---

# 気軽にDGX Sparkでapt upgradeしたら壊れた話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月17日 07:19
- **URL**: [https://zenn.dev/alpha_omega/articles/3f3ea4d14a0234](https://zenn.dev/alpha_omega/articles/3f3ea4d14a0234)

## 概要

DGX Spark で sudo apt upgrade を実行したあと、GPU ドライバがロードされなくなり、デスクトップの CPU 負荷が急増した。
復旧を試みて apt full-upgrade を実行したところ、今度は起動中とは別のカーネル向け NVIDIA モジュールがインストールされるという寄り道も発生した。
この記事では、実際に起きた状態、切り分け、復旧手順と、NVIDIA カーネルモジュールのパッケージ依存について整理する。

 結論
今回起きていたことは以下。


apt upgrade 後、カーネルが 6.17.0-1032-nvidia に更新された
一方で、そのカ...

---

*この記事は自動収集システムによって保存されました。*
