---
title: "AWS RAM で AWS KMS キーの組織共有を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-17T18:49:26
url: https://dev.classmethod.jp/articles/aws-kms-key-sharing-ram-organization/
---

# AWS RAM で AWS KMS キーの組織共有を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月17日 18:49
- **URL**: [https://dev.classmethod.jp/articles/aws-kms-key-sharing-ram-organization/](https://dev.classmethod.jp/articles/aws-kms-key-sharing-ram-organization/)

## 概要

AWS KMS のキーを AWS RAM で共有できるようになりました。対称暗号化キーを Organization 宛てに共有し、default キーポリシーを変更しないまま、Organization 内の受け側アカウントから Encrypt と Decrypt ができることを確認しました。

---

*この記事は自動収集システムによって保存されました。*
