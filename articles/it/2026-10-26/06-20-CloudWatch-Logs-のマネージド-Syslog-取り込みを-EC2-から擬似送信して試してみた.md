---
title: "CloudWatch Logs のマネージド Syslog 取り込みを EC2 から擬似送信して試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-26T06:20:41
url: https://dev.classmethod.jp/articles/cloudwatch-logs-managed-syslog-ingestion-test-from-ec2/
---

# CloudWatch Logs のマネージド Syslog 取り込みを EC2 から擬似送信して試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 06:20
- **URL**: [https://dev.classmethod.jp/articles/cloudwatch-logs-managed-syslog-ingestion-test-from-ec2/](https://dev.classmethod.jp/articles/cloudwatch-logs-managed-syslog-ingestion-test-from-ec2/)

## 概要

CloudWatch Logs の新機能「マネージド Syslog 取り込み」を検証し、VPC エンドポイント経由でオンプレミス機器のログを直接取り込める仕組みを試してみました。構築手順から実際に届いたログ、つまずいた点までをまとめます。

---

*この記事は自動収集システムによって保存されました。*
