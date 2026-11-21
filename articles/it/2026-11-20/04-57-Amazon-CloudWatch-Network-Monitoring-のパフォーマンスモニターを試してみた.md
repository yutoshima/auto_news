---
title: "Amazon CloudWatch Network Monitoring のパフォーマンスモニターを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T04:57:13
url: https://dev.classmethod.jp/articles/cloudwatch-network-monitoring-performance-monitor/
---

# Amazon CloudWatch Network Monitoring のパフォーマンスモニターを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 04:57
- **URL**: [https://dev.classmethod.jp/articles/cloudwatch-network-monitoring-performance-monitor/](https://dev.classmethod.jp/articles/cloudwatch-network-monitoring-performance-monitor/)

## 概要

VPC を指定するだけで、エージェントなしで AZ 間などのパスごとの通信量、レイテンシ、ImpactScore がコンソールと CloudWatch メトリクスに出ました。メトリクスが見えるまで約 18 分かかり、ImpactScore とレイテンシは EC2 のゲスト OS 内に入れた遅延に反応しませんでした。

---

*この記事は自動収集システムによって保存されました。*
