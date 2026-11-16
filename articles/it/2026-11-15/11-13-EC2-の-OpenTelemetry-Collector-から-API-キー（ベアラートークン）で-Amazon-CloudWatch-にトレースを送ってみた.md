---
title: "EC2 の OpenTelemetry Collector から API キー（ベアラートークン）で Amazon CloudWatch にトレースを送ってみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-15T11:13:01
url: https://dev.classmethod.jp/articles/cloudwatch-otlp-traces-api-key/
---

# EC2 の OpenTelemetry Collector から API キー（ベアラートークン）で Amazon CloudWatch にトレースを送ってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 11:13
- **URL**: [https://dev.classmethod.jp/articles/cloudwatch-otlp-traces-api-key/](https://dev.classmethod.jp/articles/cloudwatch-otlp-traces-api-key/)

## 概要

X-Ray の OTLP トレースエンドポイントで、IAM ユーザーから作成した API キーによる認証が使えるようになりました。東京リージョンで実際にトレースを送り、Logs Insights で検索できることを確認しました。

---

*この記事は自動収集システムによって保存されました。*
