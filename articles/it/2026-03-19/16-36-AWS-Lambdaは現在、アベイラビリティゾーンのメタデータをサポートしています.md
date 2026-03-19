---
title: "AWS Lambdaは現在、アベイラビリティゾーンのメタデータをサポートしています"
source: "AWS What's New"
category: "it"
published: 2026-03-19T16:36:00
url: https://aws.amazon.com/about-aws/whats-new/2026/03/lambda-availability-zone-metadata/
---

# AWS Lambdaは現在、アベイラビリティゾーンのメタデータをサポートしています

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年03月19日 16:36
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/03/lambda-availability-zone-metadata/](https://aws.amazon.com/about-aws/whats-new/2026/03/lambda-availability-zone-metadata/)

## 概要

AWS Lambdaは現在、Lambda実行環境内の新しいメタデータエンドポイントを通じて可用性ゾーン（AZ）メタデータを提供しています。この機能を使えば、Lambda関数が実行されているAZのID（例：use1-az1）を特定でき、AZを意識したルーティング判断を行う関数を構築できます。たとえば、下流サービスへの同一AZエンドポイントを優先してクロAZ待機時間を低減するなどです。この機能により、運用者はAZを前提とした運用を実現することができます。

---

*この記事は自動収集システムによって保存されました。*
