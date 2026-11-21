---
title: "Amazon EC2 Detailed Monitoring のメトリクスカテゴリで CPU 使用率を 10 秒周期で取得してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T10:13:35
url: https://dev.classmethod.jp/articles/ec2-detailed-monitoring-10-second-cpu-metrics/
---

# Amazon EC2 Detailed Monitoring のメトリクスカテゴリで CPU 使用率を 10 秒周期で取得してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 10:13
- **URL**: [https://dev.classmethod.jp/articles/ec2-detailed-monitoring-10-second-cpu-metrics/](https://dev.classmethod.jp/articles/ec2-detailed-monitoring-10-second-cpu-metrics/)

## 概要

Amazon EC2 Detailed Monitoring のメトリクスカテゴリで、CPU 使用率を 10 秒周期で取得しました。インスタンス内の設定なしで、1 分値が 33% 前後の負荷でも 10 秒値は 100% を示し、OpenTelemetry 形式の指標は PromQL で取得できました。

---

*この記事は自動収集システムによって保存されました。*
