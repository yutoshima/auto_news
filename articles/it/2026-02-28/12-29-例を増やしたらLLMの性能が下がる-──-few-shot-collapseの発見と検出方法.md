---
title: "例を増やしたらLLMの性能が下がる ── few-shot collapseの発見と検出方法"
source: "Zenn"
category: "it"
published: 2026-02-28T12:29:00
url: https://zenn.dev/okuma/articles/few_shot_collapse
---

# 例を増やしたらLLMの性能が下がる ── few-shot collapseの発見と検出方法

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月28日 12:29
- **URL**: [https://zenn.dev/okuma/articles/few_shot_collapse](https://zenn.dev/okuma/articles/few_shot_collapse)

## 概要

プロンプトに例を増やすと回答の精度が上がる、と言われています。
しかし、実際に計測してみると、例を増やすことで性能が下がるケースが見られました。
そこで、few-shot promptingで渡す例を増やしたときにモデルの性能がどう変化するかを計測するツールを作って色々と試してみました。 AdaptGauge というツール名にしてオープンソースで公開しています。

 やったこと
実務に近い以下4種のタスクに対して、shot数（例示数）を0, 1, 2, 4, 8と増やしながらLLMの性能を評価するツールにしています。


分類 — カスタマーサポートの問い合わせを8カテゴリ（請求、技術サ...

---

*この記事は自動収集システムによって保存されました。*
