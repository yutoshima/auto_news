---
title: "AWS Site-to-Site VPN がポスト量子の追加鍵交換（ML-KEM-768）に対応したので、接続して VPN ログを見てみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T14:28:46
url: https://dev.classmethod.jp/articles/aws-site-to-site-vpn-post-quantum-key-exchange/
---

# AWS Site-to-Site VPN がポスト量子の追加鍵交換（ML-KEM-768）に対応したので、接続して VPN ログを見てみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 14:28
- **URL**: [https://dev.classmethod.jp/articles/aws-site-to-site-vpn-post-quantum-key-exchange/](https://dev.classmethod.jp/articles/aws-site-to-site-vpn-post-quantum-key-exchange/)

## 概要

AWS Site-to-Site VPN がポスト量子の鍵交換に対応しました。トンネルオプションで追加鍵交換 ML-KEM-768 を指定し、strongSwan を入れた EC2 との間でトンネルを確立して、選ばれた方式を AWS 側の VPN ログと strongSwan のログで確かめました。指定方法と確認方法を紹介します。

---

*この記事は自動収集システムによって保存されました。*
