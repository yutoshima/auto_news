---
title: "AWS WAFはカスタムのリクエスト/レスポンス処理のための動的ラベル補間を導入します"
source: "AWS What's New"
category: "it"
published: 2026-05-11T18:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/05/aws-waf-dynamic-label-interpolation/
---

# AWS WAFはカスタムのリクエスト/レスポンス処理のための動的ラベル補間を導入します

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年05月11日 18:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/05/aws-waf-dynamic-label-interpolation/](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-waf-dynamic-label-interpolation/)

## 概要

AWS WAFは現在、動的ラベル補間をサポートしており、1つのルールでWAF分類信号をオリジンへ転送し、レスポンスに文脈を埋め込むことができます。以前は各信号値ごとに別のルールを維持していたセキュリティエンジニアは、カスタムリクエストヘッダー、レスポンスヘッダー、レスポンス本文で${namespace:}構文を使用して、ラベル全体のネームスペースを一括で転送できるようになります。例えば、動的変数を1つ含む1つのルールで、すべてのIP評価信号をアプリケーションへ転送できます。

---

*この記事は自動収集システムによって保存されました。*
