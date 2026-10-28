---
title: "KMS が ML-KEM 鍵をサポートしたので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-28T01:29:56
url: https://dev.classmethod.jp/articles/kms-ml-kem-key-support/
---

# KMS が ML-KEM 鍵をサポートしたので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 01:29
- **URL**: [https://dev.classmethod.jp/articles/kms-ml-kem-key-support/](https://dev.classmethod.jp/articles/kms-ml-kem-key-support/)

## 概要

AWS KMS の ML-KEM 鍵を、ECDH 鍵の置き換えとして試しました。入れ替わるのは共有秘密を作る部分だけで、HKDF と AES-256-GCM はそのまま使え、どちらも元の平文に復号できました。送信側の鍵共有は OpenSSL だけで完結します。

---

*この記事は自動収集システムによって保存されました。*
