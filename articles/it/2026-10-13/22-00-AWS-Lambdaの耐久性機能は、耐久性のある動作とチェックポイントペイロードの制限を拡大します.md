---
title: "AWS Lambdaの耐久性機能は、耐久性のある動作とチェックポイントペイロードの制限を拡大します"
source: "AWS What's New"
category: "it"
published: 2026-10-13T22:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/
---

# AWS Lambdaの耐久性機能は、耐久性のある動作とチェックポイントペイロードの制限を拡大します

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 22:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/)

## 概要

本日より、AWS Lambda の耐久性関数は、1回の実行あたりの耐久性操作の最大数を3,000から30,000に、チェックポイントペイロードの最大サイズを256 KBから1 MBにそれぞれ引き上げます。より高い操作制限により、単一の実行内でより多くの作業を安全に実行できるようになり、反復ループの拡張、長時間のポーリング、ステップが失敗した場合に実行されるより複雑なロールバック経路の構築などが可能になります。1 MBでは、チェックポイントのペイロードが非同期Lambda呼び出しの最大ペイロードサイズと同等になります。

---

*この記事は自動収集システムによって保存されました。*
