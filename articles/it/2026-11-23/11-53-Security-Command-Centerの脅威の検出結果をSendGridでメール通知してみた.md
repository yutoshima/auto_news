---
title: "Security Command Centerの脅威の検出結果をSendGridでメール通知してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-23T11:53:01
url: https://dev.classmethod.jp/articles/scc-threat-findings-sendgrid-notification/
---

# Security Command Centerの脅威の検出結果をSendGridでメール通知してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 11:53
- **URL**: [https://dev.classmethod.jp/articles/scc-threat-findings-sendgrid-notification/](https://dev.classmethod.jp/articles/scc-threat-findings-sendgrid-notification/)

## 概要

Security Command Centerの脅威の検出結果を、Pub/SubのpushサブスクリプションとCloud Run functionsを経由してSendGridでメール通知する仕組みを作りました。送信に失敗したときの再試行とアラートの動きと、SendGridのクリック計測の扱いをまとめます。

---

*この記事は自動収集システムによって保存されました。*
