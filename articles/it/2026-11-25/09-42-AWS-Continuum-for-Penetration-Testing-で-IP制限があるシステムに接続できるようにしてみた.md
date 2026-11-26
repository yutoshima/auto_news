---
title: "AWS Continuum for Penetration Testing で IP制限があるシステムに接続できるようにしてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-25T09:42:00
url: https://dev.classmethod.jp/articles/2026-11-25-security-agent-pentest-ip-allowlist/
---

# AWS Continuum for Penetration Testing で IP制限があるシステムに接続できるようにしてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 09:42
- **URL**: [https://dev.classmethod.jp/articles/2026-11-25-security-agent-pentest-ip-allowlist/](https://dev.classmethod.jp/articles/2026-11-25-security-agent-pentest-ip-allowlist/)

## 概要

IP制限があるシステムに対して、AWS Continuum for Penetration TestingにてVPC設定とNAT Gatewayで送信元IPを固定し、そのElastic IPをAWS WAFの許可リストに入れて接続し、挙動を詳細に検証しました。

---

*この記事は自動収集システムによって保存されました。*
