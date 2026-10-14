---
title: "CloudFormation で Lambda Web Functions を CloudFront OAC の背後に配置してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-13T13:33:10
url: https://dev.classmethod.jp/articles/aws-lambda-web-functions-cloudfront-oac/
---

# CloudFormation で Lambda Web Functions を CloudFront OAC の背後に配置してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 13:33
- **URL**: [https://dev.classmethod.jp/articles/aws-lambda-web-functions-cloudfront-oac/](https://dev.classmethod.jp/articles/aws-lambda-web-functions-cloudfront-oac/)

## 概要

AWS Lambda Web Functions を CloudFormation で作り、CloudFront の OAC を設定して試しました。IamAuth、OAC、リソースポリシーを組み合わせた結果、CloudFront 経由は 200、署名なしの直接アクセスは 403 でした。

---

*この記事は自動収集システムによって保存されました。*
