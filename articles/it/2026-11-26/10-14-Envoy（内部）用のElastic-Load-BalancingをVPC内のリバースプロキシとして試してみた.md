---
title: "Envoy（内部）用のElastic Load BalancingをVPC内のリバースプロキシとして試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-26T10:14:37
url: https://dev.classmethod.jp/articles/aws-elb-for-envoy-internal-path-routing/
---

# Envoy（内部）用のElastic Load BalancingをVPC内のリバースプロキシとして試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月26日 10:14
- **URL**: [https://dev.classmethod.jp/articles/aws-elb-for-envoy-internal-path-routing/](https://dev.classmethod.jp/articles/aws-elb-for-envoy-internal-path-routing/)

## 概要

`"ipv4Addressability": "internal"` で作成した ELB for Envoy に、VPC 内のクライアント EC2 からリクエストを送ると、Envoy の設定に書いたパスに応じて 2 つの内部 ALB へ振り分けられました。

---

*この記事は自動収集システムによって保存されました。*
