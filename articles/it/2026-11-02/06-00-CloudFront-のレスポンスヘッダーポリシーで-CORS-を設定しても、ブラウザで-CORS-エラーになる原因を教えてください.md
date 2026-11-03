---
title: "CloudFront のレスポンスヘッダーポリシーで CORS を設定しても、ブラウザで CORS エラーになる原因を教えてください"
source: "DevelopersIO"
category: "it"
published: 2026-11-02T06:00:15
url: https://dev.classmethod.jp/articles/tsnote-cloudfront-response-headers-policy-cors-error/
---

# CloudFront のレスポンスヘッダーポリシーで CORS を設定しても、ブラウザで CORS エラーになる原因を教えてください

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月02日 06:00
- **URL**: [https://dev.classmethod.jp/articles/tsnote-cloudfront-response-headers-policy-cors-error/](https://dev.classmethod.jp/articles/tsnote-cloudfront-response-headers-policy-cors-error/)

## 概要

CloudFront で S3 オリジンの JSON に CORS でアクセスしようとしたときに、`Access-Control-Allow-Origin` ヘッダーが正しく返らないトラブルに直面しました。原因と対策を実際に検証してみた結果を紹介します。

---

*この記事は自動収集システムによって保存されました。*
