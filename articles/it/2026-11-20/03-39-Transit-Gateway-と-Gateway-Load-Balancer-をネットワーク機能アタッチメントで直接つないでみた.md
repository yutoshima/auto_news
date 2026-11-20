---
title: "Transit Gateway と Gateway Load Balancer をネットワーク機能アタッチメントで直接つないでみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T03:39:51
url: https://dev.classmethod.jp/articles/transit-gateway-gwlb-network-function-attachment/
---

# Transit Gateway と Gateway Load Balancer をネットワーク機能アタッチメントで直接つないでみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 03:39
- **URL**: [https://dev.classmethod.jp/articles/transit-gateway-gwlb-network-function-attachment/](https://dev.classmethod.jp/articles/transit-gateway-gwlb-network-function-attachment/)

## 概要

AWS Transit Gateway の network function attachment（Gateway Load Balancer タイプ）で、GWLB エンドポイント用のサブネットとルートテーブルを作らずに通信をアプライアンスへ通せました。GENEVE パケットに付くコンテキストも確認しています。

---

*この記事は自動収集システムによって保存されました。*
