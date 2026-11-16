---
title: "Secrets Managerがクロスアカウントレプリケーションをサポートしたので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-15T14:15:25
url: https://dev.classmethod.jp/articles/secrets-manager-cross-account-replication/
---

# Secrets Managerがクロスアカウントレプリケーションをサポートしたので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 14:15
- **URL**: [https://dev.classmethod.jp/articles/secrets-manager-cross-account-replication/](https://dev.classmethod.jp/articles/secrets-manager-cross-account-replication/)

## 概要

AWS Secrets Manager のクロスアカウントレプリケーションを2つのアカウントで試しました。レプリカ側に KMS キーを用意して関連付けると、プライマリの更新が1秒ほどでレプリカに届き、レプリカ側で昇格させると単独のシークレットとして使えました。

---

*この記事は自動収集システムによって保存されました。*
