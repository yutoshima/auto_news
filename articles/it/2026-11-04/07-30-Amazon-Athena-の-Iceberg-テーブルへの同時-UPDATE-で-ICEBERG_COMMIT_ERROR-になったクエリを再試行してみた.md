---
title: "Amazon Athena の Iceberg テーブルへの同時 UPDATE で ICEBERG_COMMIT_ERROR になったクエリを再試行してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-04T07:30:11
url: https://dev.classmethod.jp/articles/athena-iceberg-update-commit-error-exponential-backoff/
---

# Amazon Athena の Iceberg テーブルへの同時 UPDATE で ICEBERG_COMMIT_ERROR になったクエリを再試行してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月04日 07:30
- **URL**: [https://dev.classmethod.jp/articles/athena-iceberg-update-commit-error-exponential-backoff/](https://dev.classmethod.jp/articles/athena-iceberg-update-commit-error-exponential-backoff/)

## 概要

Amazon Athena で Iceberg テーブルへ複数のクライアントから同時に UPDATE すると、`ICEBERG_COMMIT_ERROR` で失敗することがあります。この失敗の実際の起こり方と、効果的な再試行の方法を、実験を通じて確かめてみました。

---

*この記事は自動収集システムによって保存されました。*
