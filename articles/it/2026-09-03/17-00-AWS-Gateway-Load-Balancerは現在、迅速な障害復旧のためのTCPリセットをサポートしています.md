---
title: "AWS Gateway Load Balancerは現在、迅速な障害復旧のためのTCPリセットをサポートしています"
source: "AWS What's New"
category: "it"
published: 2026-09-03T17:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/
---

# AWS Gateway Load Balancerは現在、迅速な障害復旧のためのTCPリセットをサポートしています

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月03日 17:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/)

## 概要

<p>A<b></b>WS Gateway Load Balancer (GWLB) は、ターゲットが不健康になる、登録解除される、またはフローのアイドルタイムアウトが期限切れになるときに、TCPリセット（RST）パケットを送信することをサポートします。この機能により、TCPエンドポイントが接続の失敗を迅速に検知し、健全なターゲットを介して新しいTCPフローを確立できるようにすることで、トラフィックの中断を数分から数秒に短縮します。<br /> <br /> 以前は、GWLBターゲットが失敗した場合、既存のTCP接続は不健康なターゲットへ転送され続けていました（ak

---

*この記事は自動収集システムによって保存されました。*
