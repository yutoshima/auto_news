---
title: "AWS Network Firewall に NAT Gateway を関連付けて、明示的プロキシを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-23T19:19:57
url: https://dev.classmethod.jp/articles/aws-network-firewall-proxy-nat-gateway/
---

# AWS Network Firewall に NAT Gateway を関連付けて、明示的プロキシを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 19:19
- **URL**: [https://dev.classmethod.jp/articles/aws-network-firewall-proxy-nat-gateway/](https://dev.classmethod.jp/articles/aws-network-firewall-proxy-nat-gateway/)

## 概要

東京リージョンで AWS Network Firewall に NAT Gateway を関連付けて明示的プロキシとして設定し、curl にプロキシを指定した通信を DNS と TLS SNI のルールでドメインごとに許可・拒否できることを確認しました。送信元 IP は NAT Gateway の Elastic IP でした。

---

*この記事は自動収集システムによって保存されました。*
