---
title: "AWS Gateway Load BalancerがTCPリセットをサポートし、障害回復を迅速化します"
source: "AWS What's New"
category: "it"
published: 2026-09-03T17:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/
---

# AWS Gateway Load BalancerがTCPリセットをサポートし、障害回復を迅速化します

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月03日 17:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/)

## 概要

<p>A<b></b>WS Gateway Load Balancer (GWLB) は、ターゲットが非健康状態になった場合、登録解除された場合、またはフローのアイドルタイムアウトが切れた場合に、TCPリセット（RST）パケットを送信することをサポートします。この機能により、TCPエンドポイントが失敗した接続を迅速に検出し、健全なターゲットを通じて新しいTCPフローを確立できるようにすることで、トラフィックの中断を分からずのレベルから秒単位へ短縮します。<br /> <br /> 以前は、GWLBのターゲットが失敗した場合、既存のTCP接続は非健全なターゲットへ転送され続けていました（ak

---

*この記事は自動収集システムによって保存されました。*
