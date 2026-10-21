---
title: "CloudFront の Origin Shield で S3 へのクロスリージョン参照性能が改善するか試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-20T19:19:53
url: https://dev.classmethod.jp/articles/cloudfront-origin-shield-s3-cross-region-latency/
---

# CloudFront の Origin Shield で S3 へのクロスリージョン参照性能が改善するか試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月20日 19:19
- **URL**: [https://dev.classmethod.jp/articles/cloudfront-origin-shield-s3-cross-region-latency/](https://dev.classmethod.jp/articles/cloudfront-origin-shield-s3-cross-region-latency/)

## 概要

Lambda Web Functions で別リージョンの S3 を参照したときの遅延改善に、Origin Shield が有効かを検証しました。エッジにキャッシュがない状態でも、クロスリージョンの取得時間が p50 で 170〜330ms 改善しました。

---

*この記事は自動収集システムによって保存されました。*
