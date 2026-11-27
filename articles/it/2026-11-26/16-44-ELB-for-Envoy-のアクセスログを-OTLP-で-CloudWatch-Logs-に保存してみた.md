---
title: "ELB for Envoy のアクセスログを OTLP で CloudWatch Logs に保存してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-26T16:44:34
url: https://dev.classmethod.jp/articles/elb-for-envoy-access-log-cloudwatch-logs/
---

# ELB for Envoy のアクセスログを OTLP で CloudWatch Logs に保存してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月26日 16:44
- **URL**: [https://dev.classmethod.jp/articles/elb-for-envoy-access-log-cloudwatch-logs/](https://dev.classmethod.jp/articles/elb-for-envoy-access-log-cloudwatch-logs/)

## 概要

open_telemetry の access logger から、設定に認証情報を書かずに、SigV4 の署名で東京リージョンの CloudWatch Logs の OTLP エンドポイントへアクセスログを送って保存できました。保存されるログ形式や項目の設定もまとめています。

---

*この記事は自動収集システムによって保存されました。*
