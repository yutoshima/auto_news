---
title: "Reservoir Computing で公開ベンチマークの異常検知をやってみる"
source: "Zenn"
category: "it"
published: 2026-10-12T01:49:27
url: https://zenn.dev/kotton_mas/articles/rc-basics-05-anomaly-detection
---

# Reservoir Computing で公開ベンチマークの異常検知をやってみる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月12日 01:49
- **URL**: [https://zenn.dev/kotton_mas/articles/rc-basics-05-anomaly-detection](https://zenn.dev/kotton_mas/articles/rc-basics-05-anomaly-detection)

## 概要

はじめに
今までの記事では自分で作った合成データだけでしたが、今回は外部の公開ベンチマークを使います。MGAB (Mackey-Glass Anomaly Benchmark) です。
先に正直に書いておくと、MGAB は「実データ」ではありません。Mackey-Glass 系列に人工的な異常区間を挿入して作られた合成ベンチマークです。実データ (UCR Anomaly Archive) も候補にはしたのですが、今回は回していません。理由は最後に書きます。
やることは単純で、ESN で1ステップ先を予測して、その残差の異常さでアラートを出すというもの。
スコアの系統を6つ並べました。...

---

*この記事は自動収集システムによって保存されました。*
