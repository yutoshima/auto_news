---
title: "AWS Network Load Balancerは現在、カスタムトラフィックルーティングのためのリスナールールをサポートしています"
source: "AWS What's New"
category: "it"
published: 2026-07-22T19:13:00
url: https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/
---

# AWS Network Load Balancerは現在、カスタムトラフィックルーティングのためのリスナールールをサポートしています

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年07月22日 19:13
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/)

## 概要

ネットワーク負荷 balancer（NLB）は、ソースIPアドレスのタイプに基づいて接続を異なるターゲットグループへルーティングするリスナー規則をサポートするようになりました。リスナー規則を使用すると、単一のデュアルスタックNLBがIPv6クライアントトラフィックをIPv6ターゲットへ、IPv4クライアントトラフィックをIPv4ターゲットへ送信し、両方のアドレスタイプに対してエンドツーエンドで元のクライアントIPアドレスを保持します。

以前は、1つのNLBからIPv4およびIPv6クライアントの両方を処理するには、次のいずれかのトレードオフを受け入れる必要がありました。別々のロードバランサを運用するか、または一方のアドレスファミリのクライアントのための情報が失われるか、という選択でした。

---

*この記事は自動収集システムによって保存されました。*
