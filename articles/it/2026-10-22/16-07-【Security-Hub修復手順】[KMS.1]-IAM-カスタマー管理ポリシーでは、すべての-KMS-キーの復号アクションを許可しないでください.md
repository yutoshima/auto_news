---
title: "【Security Hub修復手順】[KMS.1] IAM カスタマー管理ポリシーでは、すべての KMS キーの復号アクションを許可しないでください"
source: "DevelopersIO"
category: "it"
published: 2026-10-22T16:07:46
url: https://dev.classmethod.jp/articles/securityhub-fsbp-remediation-kms-1/
---

# 【Security Hub修復手順】[KMS.1] IAM カスタマー管理ポリシーでは、すべての KMS キーの復号アクションを許可しないでください

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 16:07
- **URL**: [https://dev.classmethod.jp/articles/securityhub-fsbp-remediation-kms-1/](https://dev.classmethod.jp/articles/securityhub-fsbp-remediation-kms-1/)

## 概要

AWS Security Hubの「KMS.1」コントロールに対応するため、IAMカスタマー管理ポリシーでKMS復号アクションの権限を特定キーに限定する修復手順をご紹介します。

---

*この記事は自動収集システムによって保存されました。*
