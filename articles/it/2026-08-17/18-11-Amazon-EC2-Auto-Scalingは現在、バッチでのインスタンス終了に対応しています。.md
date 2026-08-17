---
title: "Amazon EC2 Auto Scalingは現在、バッチでのインスタンス終了に対応しています。"
source: "AWS What's New"
category: "it"
published: 2026-08-17T18:11:00
url: https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-auto-scaling-batch-termination
---

# Amazon EC2 Auto Scalingは現在、バッチでのインスタンス終了に対応しています。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年08月17日 18:11
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-auto-scaling-batch-termination](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-auto-scaling-batch-termination)

## 概要

Amazon EC2 Auto Scalingは現在、1つのAPI呼び出しで batch インスタンス終了をサポートしています。Terminat eInstanceInAutoScalingGroup APIに最大100個のインスタンスIDを渡すことで、それらをバッチとして終了させ、Auto Scalingグループを縮小する際に必要なAPI呼び出しの回数を減らすことができます。

バッチ終了は、AI/MLトレーニングジョブ、コンテナオーケストレーター、または一時的に大量のインスタンスを起動するイベント駆動型アーキテクチャなど、急速に縮小する必要のあるワークロード向けに設計されています。すべては

---

*この記事は自動収集システムによって保存されました。*
