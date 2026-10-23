---
title: "【Security Hub修復手順】[KMS.2] IAM プリンシパルは、すべての KMS キーで復号アクションを許可する IAM インラインポリシーを使用しないでください"
source: "DevelopersIO"
category: "it"
published: 2026-10-22T16:06:57
url: https://dev.classmethod.jp/articles/securityhub-fsbp-remediation-kms-2/
---

# 【Security Hub修復手順】[KMS.2] IAM プリンシパルは、すべての KMS キーで復号アクションを許可する IAM インラインポリシーを使用しないでください

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 16:06
- **URL**: [https://dev.classmethod.jp/articles/securityhub-fsbp-remediation-kms-2/](https://dev.classmethod.jp/articles/securityhub-fsbp-remediation-kms-2/)

## 概要

AWS Security HubのKMS.2コントロールで検出されたIAMインラインポリシーの修復手順をご紹介します。すべてのKMSキーへの復号を許可するポリシーを特定のキーに限定する方法を、実際の設定例とともに説明します。

---

*この記事は自動収集システムによって保存されました。*
