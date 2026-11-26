---
title: "Security Hub CSPM の通知を PreviousComplianceStatus で抑える方法を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-25T10:02:41
url: https://dev.classmethod.jp/articles/securityhub-eventbridge-previous-compliance-status/
---

# Security Hub CSPM の通知を PreviousComplianceStatus で抑える方法を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 10:02
- **URL**: [https://dev.classmethod.jp/articles/securityhub-eventbridge-previous-compliance-status/](https://dev.classmethod.jp/articles/securityhub-eventbridge-previous-compliance-status/)

## 概要

AWS Security Hub CSPM のコントロールが FAILED に変わったときだけ EventBridge で通知するために、ProductFields の PreviousComplianceStatus で絞り込んでみました。作られたばかりの検出結果にはこのフィールドが無い点にも注意が必要でした。

---

*この記事は自動収集システムによって保存されました。*
