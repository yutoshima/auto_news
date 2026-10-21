---
title: "S3 の Multi-Region Access Points でクロスリージョン参照性能が改善するか試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-20T21:03:12
url: https://dev.classmethod.jp/articles/s3-multi-region-access-points-cross-region-latency/
---

# S3 の Multi-Region Access Points でクロスリージョン参照性能が改善するか試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月20日 21:03
- **URL**: [https://dev.classmethod.jp/articles/s3-multi-region-access-points-cross-region-latency/](https://dev.classmethod.jp/articles/s3-multi-region-access-points-cross-region-latency/)

## 概要

複数リージョンの Lambda からバージニア北部（us-east-1）の S3 を参照する構成で、Amazon S3 Multi-Region Access Points（MRAP）を使うと取得時間がどう変わるかを測りました。us-east-1 以外のリージョンでは p50 が 58〜83%（S3 API）、76〜92%（CloudFront 経由、キャッシュなし）短くなりました。

---

*この記事は自動収集システムによって保存されました。*
