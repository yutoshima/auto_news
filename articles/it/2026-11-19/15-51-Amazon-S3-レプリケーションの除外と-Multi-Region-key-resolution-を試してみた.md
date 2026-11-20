---
title: "Amazon S3 レプリケーションの除外と Multi-Region key resolution を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T15:51:24
url: https://dev.classmethod.jp/articles/s3-replication-exclusions-multi-region-key/
---

# Amazon S3 レプリケーションの除外と Multi-Region key resolution を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 15:51
- **URL**: [https://dev.classmethod.jp/articles/s3-replication-exclusions-multi-region-key/](https://dev.classmethod.jp/articles/s3-replication-exclusions-multi-region-key/)

## 概要

Amazon S3 レプリケーションの除外と Multi-Region key resolution を、東京からバージニア北部への複製で試しました。プレフィックスの除外は、Filter の Not で指定できました。別々のマルチリージョンキーで暗号化したオブジェクトは、1つのルールで複製されました。

---

*この記事は自動収集システムによって保存されました。*
