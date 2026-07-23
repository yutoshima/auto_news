---
title: "AWS Network Load Balancerは現在、カスタムトラフィックルーティングのためのリスナールールをサポートします"
source: "AWS What's New"
category: "it"
published: 2026-07-22T19:13:00
url: https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/
---

# AWS Network Load Balancerは現在、カスタムトラフィックルーティングのためのリスナールールをサポートします

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年07月22日 19:13
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/)

## 概要

ネットワークロードバランサー（NLB）は、ソースIPアドレスの種類に基づいて異なるターゲットグループへ接続をルーティングするリスナー規則をサポートするようになりました。リスナー規則を使用すると、単一のデュアルスタックNLBがIPv6クライアントトラフィックをIPv6ターゲットへ、IPv4クライアントトラフィックをIPv4ターゲットへ送信し、両方のアドレスタイプについてエンドツーエンドで元のクライアントIPアドレスを保持します。

以前は、1つのNLBからIPv4およびIPv6クライアントの両方を処理するには、トレードオフを受け入れる必要がありました。すなわち、2つの別々のロードバランサーを実行するかどうか、という選択を迫られていました。

---

*この記事は自動収集システムによって保存されました。*
