---
title: "ELBを経由して Envoy から Aurora（PostgreSQL / MySQL）へのDB接続を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-27T17:34:52
url: https://dev.classmethod.jp/articles/elb-for-envoy-aurora-tcp-proxy/
---

# ELBを経由して Envoy から Aurora（PostgreSQL / MySQL）へのDB接続を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月27日 17:34
- **URL**: [https://dev.classmethod.jp/articles/elb-for-envoy-aurora-tcp-proxy/](https://dev.classmethod.jp/articles/elb-for-envoy-aurora-tcp-proxy/)

## 概要

Aurora PostgreSQL は、ELB for Envoy の tcp_proxy 経由で EC2 から接続できました。Aurora MySQL は、フィルターのタイムアウト後も接続を維持する指定により接続できました。

---

*この記事は自動収集システムによって保存されました。*
