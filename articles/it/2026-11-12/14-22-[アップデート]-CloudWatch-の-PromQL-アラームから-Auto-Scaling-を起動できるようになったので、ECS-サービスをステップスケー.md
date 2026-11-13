---
title: "[アップデート] CloudWatch の PromQL アラームから Auto Scaling を起動できるようになったので、ECS サービスをステップスケーリングしてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-12T14:22:20
url: https://dev.classmethod.jp/articles/try-cloudwatch-promql-alarm-ecs-step-scaling/
---

# [アップデート] CloudWatch の PromQL アラームから Auto Scaling を起動できるようになったので、ECS サービスをステップスケーリングしてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月12日 14:22
- **URL**: [https://dev.classmethod.jp/articles/try-cloudwatch-promql-alarm-ecs-step-scaling/](https://dev.classmethod.jp/articles/try-cloudwatch-promql-alarm-ecs-step-scaling/)

## 概要

Amazon CloudWatch の PromQL アラームから Application Auto Scaling のステップスケーリングポリシーを起動し、OpenTelemetry のカスタムメトリクスで Amazon ECS サービスのタスク数が増減するところまで確かめました。しきい値の超過幅ごとのステップと所要時間の実測、クエリの形の制約やターゲット追跡ポリシーなどの注意点をまとめています。

---

*この記事は自動収集システムによって保存されました。*
