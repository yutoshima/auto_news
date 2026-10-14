---
title: "Lambda Web Functions を CloudFront OAC で保護すると、POST / PUT の x-amz-content-sha256 が不要になる"
source: "DevelopersIO"
category: "it"
published: 2026-10-13T03:02:17
url: https://dev.classmethod.jp/articles/shuntaka-lambda-web-functions-cloudfront-oac/
---

# Lambda Web Functions を CloudFront OAC で保護すると、POST / PUT の x-amz-content-sha256 が不要になる

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 03:02
- **URL**: [https://dev.classmethod.jp/articles/shuntaka-lambda-web-functions-cloudfront-oac/](https://dev.classmethod.jp/articles/shuntaka-lambda-web-functions-cloudfront-oac/)

## 概要

AWS Lambdaに新しく追加されたWeb Functionsを、CloudFront OACと組み合わせてHonoで実装してみました。POST・Authorizationヘッダー・ストリーミングの挙動を確認します。

---

*この記事は自動収集システムによって保存されました。*
