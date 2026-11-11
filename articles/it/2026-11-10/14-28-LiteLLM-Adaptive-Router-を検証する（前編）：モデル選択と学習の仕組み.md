---
title: "LiteLLM Adaptive Router を検証する（前編）：モデル選択と学習の仕組み"
source: "Zenn"
category: "it"
published: 2026-11-10T14:28:03
url: https://zenn.dev/aws_japan/articles/ac9ae548d57323
---

# LiteLLM Adaptive Router を検証する（前編）：モデル選択と学習の仕組み

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 14:28
- **URL**: [https://zenn.dev/aws_japan/articles/ac9ae548d57323](https://zenn.dev/aws_japan/articles/ac9ae548d57323)

## 概要

はじめに
LiteLLM の Adaptive Router（auto_router/adaptive_router、BETA）は、1つのモデル名で受け付けたリクエストを、内容に応じて複数のモデルへ振り分けます。モデルの品質とコストを評価し、会話から得た反応を以後の選択に反映します。
公式ドキュメントだけでは、次の仕様を把握しにくい状態です。

モデル選択で参照する情報

weights（品質とコストの重み）が選択結果に与える影響
学習に使用するシグナルと、学習が発生しない条件
日本語プロンプトの分類と学習
運用時に考慮すべき制約

本記事では、LiteLLM v1.106.2 の ...

---

*この記事は自動収集システムによって保存されました。*
