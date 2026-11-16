---
title: "EC2 の ImdsV1Enabled メトリクスで IMDSv2 を必須にしていないインスタンスを特定してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-15T15:12:18
url: https://dev.classmethod.jp/articles/ec2-imdsv1enabled-metric/
---

# EC2 の ImdsV1Enabled メトリクスで IMDSv2 を必須にしていないインスタンスを特定してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 15:12
- **URL**: [https://dev.classmethod.jp/articles/ec2-imdsv1enabled-metric/](https://dev.classmethod.jp/articles/ec2-imdsv1enabled-metric/)

## 概要

Amazon EC2 の CloudWatch メトリクス ImdsV1Enabled で、IMDSv2 を必須にしていないインスタンスを特定できるか試しました。get-metric-data の SEARCH を使うと3台分の値を1回の問い合わせで取得でき、required に変更すると、今回の3回ではいずれも4分59秒以内に 0 が見えました。

---

*この記事は自動収集システムによって保存されました。*
