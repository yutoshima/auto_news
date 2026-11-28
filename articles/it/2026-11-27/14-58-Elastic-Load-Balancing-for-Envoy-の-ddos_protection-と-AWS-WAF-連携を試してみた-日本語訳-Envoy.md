---
title: "Elastic Load Balancing for Envoy の ddos_protection と AWS WAF 連携を試してみた\n\n日本語訳:\nEnvoy 用の Elastic Load Balancing の ddos_protection と AWS WAF の連携を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-27T14:58:20
url: https://dev.classmethod.jp/articles/aws-elb-for-envoy-syn-cookie-waf/
---

# Elastic Load Balancing for Envoy の ddos_protection と AWS WAF 連携を試してみた

日本語訳:
Envoy 用の Elastic Load Balancing の ddos_protection と AWS WAF の連携を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月27日 14:58
- **URL**: [https://dev.classmethod.jp/articles/aws-elb-for-envoy-syn-cookie-waf/](https://dev.classmethod.jp/articles/aws-elb-for-envoy-syn-cookie-waf/)

## 概要

ddos_protection の SYN cookie mode を continuous にすると、SYN-ACK の形が変わり、不正な ACK に SYN-ACK を再送しなくなりました。AWS WAF の Block ルール（IP 指定、レートルール）による遮断も確認できました。

---

*この記事は自動収集システムによって保存されました。*
