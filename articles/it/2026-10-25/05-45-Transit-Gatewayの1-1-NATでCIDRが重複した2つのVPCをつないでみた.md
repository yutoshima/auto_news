---
title: "Transit Gatewayの1:1 NATでCIDRが重複した2つのVPCをつないでみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-25T05:45:24
url: https://dev.classmethod.jp/articles/transit-gateway-1to1-nat-overlapping-cidr/
---

# Transit Gatewayの1:1 NATでCIDRが重複した2つのVPCをつないでみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 05:45
- **URL**: [https://dev.classmethod.jp/articles/transit-gateway-1to1-nat-overlapping-cidr/](https://dev.classmethod.jp/articles/transit-gateway-1to1-nat-overlapping-cidr/)

## 概要

Transit Gateway の 1:1 NAT で、同じ CIDR（10.0.0.0/16）の 2 つの VPC をつないでみました。両方のアタッチメントにルールを 1 つずつ設定すると、NAT 用のリソースを足さずに通信でき、受信側には変換後のアドレスが送信元として届きました。

---

*この記事は自動収集システムによって保存されました。*
