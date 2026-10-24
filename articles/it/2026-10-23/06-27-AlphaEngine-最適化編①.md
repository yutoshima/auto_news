---
title: "AlphaEngine: 最適化編①"
source: "Zenn"
category: "it"
published: 2026-10-23T06:27:00
url: https://zenn.dev/reu/articles/f79a89bd44b541
---

# AlphaEngine: 最適化編①

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 06:27
- **URL**: [https://zenn.dev/reu/articles/f79a89bd44b541](https://zenn.dev/reu/articles/f79a89bd44b541)

## 概要

はじめに
今回は、Static/Skeletalメッシュの分離による頂点処理およびAcceleration Structure更新処理の改善をどうしたかを書いていきたいと思います。

 以前の実装と問題点
Static/Skeletalを区別せず、全頂点をCompute Shaderで処理してBLASを更新していました。
理由としては、AlphaEngineのレンダリングの設計思想としてあった
「全ての処理を一元化したい」
という部分を強く見すぎた結果でした。
その結果、本来処理をしないでいいStaticモデルも強制的にBLASの更新も行ってしまうという
ゲーム的にもやりたくないよね...

---

*この記事は自動収集システムによって保存されました。*
