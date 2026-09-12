---
title: "Amazon SageMaker HyperPodは、推論の自動スケーリングを高速化し、コールドスタートを減らすためのモデルキャッシュをサポートします"
source: "AWS What's New"
category: "it"
published: 2026-09-11T18:25:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/sgm-hyperpod-model-caching-inf/
---

# Amazon SageMaker HyperPodは、推論の自動スケーリングを高速化し、コールドスタートを減らすためのモデルキャッシュをサポートします

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月11日 18:25
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/sgm-hyperpod-model-caching-inf/](https://aws.amazon.com/about-aws/whats-new/2026/09/sgm-hyperpod-model-caching-inf/)

## 概要

<p>Amazon SageMaker HyperPod は現在、モデルキャッシュをサポートしています。これは、クラスターのノード上にモデルの重みとコンテナイメージをあらかじめロードしておく推論最適化で、ポッドが数十秒ではなく数分かかる開始を数秒に短縮します。</p>
<p>チャットアシスタント、エージェンティック・パイプライン、RAG、ドキュメント分析などのワークロードで大規模にLLM推論を実行する場合、コールドスタートは実際のボトルネックとなります。デプロイメントとスケールアウトイベントは、ほとんどの時間をコンテナイメージとモデル重みのダウンロードに費やします。モデルサイズが大きくなるにつれて、これがさらに顕著になります。</p>

---

*この記事は自動収集システムによって保存されました。*
