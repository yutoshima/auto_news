---
title: "Amazon CloudWatch Observability EKS アドオンは、カスタム OpenTelemetry および Prometheus テレメトリをサポートしました"
source: "AWS What's New"
category: "it"
published: 2026-11-20T20:05:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-addon-custom-telemetry/
---

# Amazon CloudWatch Observability EKS アドオンは、カスタム OpenTelemetry および Prometheus テレメトリをサポートしました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 20:05
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-addon-custom-telemetry/](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-addon-custom-telemetry/)

## 概要

本日、Amazon CloudWatchはCloudWatch Observability EKSアドオンにおける独自アプリケーションのテレメトリのサポートを発表します。すでに実行しているCloudWatchエージェントは、これまで通りアプリケーションからのメトリクス、トレース、ログを受け付けるため、CloudWatchに取り込むための別個のコレクターをデプロイ・運用する必要がなくなります。

OpenTelemetry SDKで計測されるアプリケーションは、エージェントが各ノード上でデフォルトで提供するOTLPエンドポイントへ送信します。メトリクスは、PromQLでクエリできるCloudWatchメトリクスとして到着します。

---

*この記事は自動収集システムによって保存されました。*
