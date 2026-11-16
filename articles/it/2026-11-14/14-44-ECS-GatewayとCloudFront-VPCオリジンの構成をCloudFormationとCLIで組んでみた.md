---
title: "ECS GatewayとCloudFront VPCオリジンの構成をCloudFormationとCLIで組んでみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-14T14:44:30
url: https://dev.classmethod.jp/articles/ecs-gateway-cloudfront-vpc-origin-cfn/
---

# ECS GatewayとCloudFront VPCオリジンの構成をCloudFormationとCLIで組んでみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月14日 14:44
- **URL**: [https://dev.classmethod.jp/articles/ecs-gateway-cloudfront-vpc-origin-cfn/](https://dev.classmethod.jp/articles/ecs-gateway-cloudfront-vpc-origin-cfn/)

## 概要

ECS Gateway と CloudFront VPC オリジンの構成を CloudFormation で組みました。ECS Gateway の ALB の ARN など、スタック作成直後に存在しない値の参照は、CLI で取得してパラメータとして渡す形で回避しました。

---

*この記事は自動収集システムによって保存されました。*
