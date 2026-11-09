---
title: "AWS Network Firewall の Reject と Alert のドメインリストを Allow と組み合わせ、ルールの評価順序ごとに確かめてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-08T05:33:38
url: https://dev.classmethod.jp/articles/network-firewall-domain-list-reject-alert-rule-order/
---

# AWS Network Firewall の Reject と Alert のドメインリストを Allow と組み合わせ、ルールの評価順序ごとに確かめてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月08日 05:33
- **URL**: [https://dev.classmethod.jp/articles/network-firewall-domain-list-reject-alert-rule-order/](https://dev.classmethod.jp/articles/network-firewall-domain-list-reject-alert-rule-order/)

## 概要

AWS Network Firewall のドメインリストルールグループで、Allow・Reject・Alert を組み合わせた場合の動作を実際に検証してみました。ドキュメントで推奨されている設定の効果を、curl の結果とログの記録状況から確認しています。

---

*この記事は自動収集システムによって保存されました。*
