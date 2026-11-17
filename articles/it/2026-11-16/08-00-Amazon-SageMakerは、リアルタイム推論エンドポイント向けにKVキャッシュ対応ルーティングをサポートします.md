---
title: "Amazon SageMakerは、リアルタイム推論エンドポイント向けにKVキャッシュ対応ルーティングをサポートします"
source: "AWS What's New"
category: "it"
published: 2026-11-16T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-kv-cache-routing/
---

# Amazon SageMakerは、リアルタイム推論エンドポイント向けにKVキャッシュ対応ルーティングをサポートします

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月16日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-kv-cache-routing/](https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-kv-cache-routing/)

## 概要

<p>Amazon SageMaker AIは現在、リアルタイム推論エンドポイントのKVキャッシュ対応ルーティングをサポートしており、長いプロンプトや繰り返しのプロンプトを含むLLMワークロードで最初のトークンまでの待機時間を短縮できます。vLLMなどのサービングエンジンは、共有システムプロンプト、文書、会話履歴といった繰り返しの開始時のプロンプトのために計算済みのキー値(KV)キャッシュを保存し、繰り返しの処理をスキップします。複数のインスタンスにまたがって、キャッシュが欠如している場所へ着地したリクエストは再計算します。高負荷時には、インスタンスがキャッシュを追い出す場合もあります。

---

*この記事は自動収集システムによって保存されました。*
