---
title: "【アップデート】Network Firewall の SNI 詐称対策が強化されたので、再現して確かめてみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-22T06:29:58
url: https://dev.classmethod.jp/articles/network-firewall-resolved-ip-validation/
---

# 【アップデート】Network Firewall の SNI 詐称対策が強化されたので、再現して確かめてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 06:29
- **URL**: [https://dev.classmethod.jp/articles/network-firewall-resolved-ip-validation/](https://dev.classmethod.jp/articles/network-firewall-resolved-ip-validation/)

## 概要

AWS Network Firewall の Route 53 Resolved IP validation で、SNI 詐称を試しました。標準のドメインルールだけでは通った詐称が、ポリシーを DROP にすると止まり、名前解決した example.com への接続は通りました。

---

*この記事は自動収集システムによって保存されました。*
