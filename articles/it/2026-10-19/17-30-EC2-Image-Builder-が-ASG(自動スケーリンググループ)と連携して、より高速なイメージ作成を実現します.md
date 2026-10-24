---
title: "EC2 Image Builder が ASG(自動スケーリンググループ)と連携して、より高速なイメージ作成を実現します"
source: "AWS What's New"
category: "it"
published: 2026-10-19T17:30:00
url: https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-image-builder-asg-faster-builds/
---

# EC2 Image Builder が ASG(自動スケーリンググループ)と連携して、より高速なイメージ作成を実現します

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年10月19日 17:30
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-image-builder-asg-faster-builds/](https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-image-builder-asg-faster-builds/)

## 概要

EC2 Image Builderは現在、イメージ作成時にASG（Auto Scaling Group）から既存のインスタンスを使用することをサポートしています。新しいインスタンスを起動してブートストラップするのに要する時間を省き、すでに実行中のEC2インスタンスを再利用することで、ビルドを高速化します。

この機能を使うと、Image Builderのインフラストラクチャ設定にASGを指定できます。ビルド時に新しいインスタンスを起動する代わりに、ASG内のすでに実行中のインスタンスをImage Builderが選択し、ビルド構成を適用します。

---

*この記事は自動収集システムによって保存されました。*
