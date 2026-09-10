---
title: "Cluster Autoscaler から Karpenter へ移行して分かったこと"
source: "Zenn"
category: "it"
published: 2026-09-09T01:09:17
url: https://zenn.dev/socialplus/articles/dc1ceeb1e42edc
---

# Cluster Autoscaler から Karpenter へ移行して分かったこと

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月09日 01:09
- **URL**: [https://zenn.dev/socialplus/articles/dc1ceeb1e42edc](https://zenn.dev/socialplus/articles/dc1ceeb1e42edc)

## 概要

概要
弊社ではノードオートスケーラーとして Cluster Autoscaler を使っていましたが、AZ 分割 Node Group の運用負債や EKS Auto Mode への移行検討などをきっかけに、Karpenter への全面移行を行いました。
移行によって、AZ ごとに Node Group を分割する必要がなくなり運用がシンプルになったほか、consolidation によるノードの最適化（余ったノードの削減や、過剰スペックなノードをより適切なインスタンスタイプに詰め替える動き）で狙い通りコスト最適化の効果も得られました。
一方で、期待していたスケールアウト速度の向上は...

---

*この記事は自動収集システムによって保存されました。*
