---
title: "RDS Proxyの認証設定を変更したときに、既存の接続に影響はあるのか確かめてみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-26T00:37:33
url: https://dev.classmethod.jp/articles/202610-rds-proxy-auth-change-existing-connections/
---

# RDS Proxyの認証設定を変更したときに、既存の接続に影響はあるのか確かめてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 00:37
- **URL**: [https://dev.classmethod.jp/articles/202610-rds-proxy-auth-change-existing-connections/](https://dev.classmethod.jp/articles/202610-rds-proxy-auth-change-existing-connections/)

## 概要

稼働中のRDS Proxyで、シークレットを追加・削除したり、クライアント認証タイプを変更したりしたときに、既存の接続に影響はあるのかをAurora PostgreSQLで確かめてみました。

---

*この記事は自動収集システムによって保存されました。*
