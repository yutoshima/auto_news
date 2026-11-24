---
title: "CloudFront マルチテナントで stg と prod を分けて静的サイトを配信してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-23T13:00:08
url: https://dev.classmethod.jp/articles/cloudfront-multitenant-stg-prod/
---

# CloudFront マルチテナントで stg と prod を分けて静的サイトを配信してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 13:00
- **URL**: [https://dev.classmethod.jp/articles/cloudfront-multitenant-stg-prod/](https://dev.classmethod.jp/articles/cloudfront-multitenant-stg-prod/)

## 概要

CloudFront のマルチテナントディストリビューションを使って、1つのディストリビューションで stg と prod を分けて管理する構成を試しました。開発環境には Basic 認証をかけ、本番環境は認証なしで公開する、という要件を実装しています。

---

*この記事は自動収集システムによって保存されました。*
