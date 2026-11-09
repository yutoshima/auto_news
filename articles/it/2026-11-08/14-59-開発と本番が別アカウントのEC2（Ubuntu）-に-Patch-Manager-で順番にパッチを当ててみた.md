---
title: "開発と本番が別アカウントのEC2（Ubuntu） に Patch Manager で順番にパッチを当ててみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-08T14:59:48
url: https://dev.classmethod.jp/articles/shoma-applied-patches-sequentially-with-patch-manager-to-ubuntu-ec2-in-separate-dev-and-prod-accounts/
---

# 開発と本番が別アカウントのEC2（Ubuntu） に Patch Manager で順番にパッチを当ててみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月08日 14:59
- **URL**: [https://dev.classmethod.jp/articles/shoma-applied-patches-sequentially-with-patch-manager-to-ubuntu-ec2-in-separate-dev-and-prod-accounts/](https://dev.classmethod.jp/articles/shoma-applied-patches-sequentially-with-patch-manager-to-ubuntu-ec2-in-separate-dev-and-prod-accounts/)

## 概要

前回設計したUbuntu 24.04のパッチ運用ルールを、開発と本番の2つのAWSアカウントで実際に構築・検証してみます。セキュリティ更新の承認から本番への適用まで、各ステップを手動で動かしながら仕組みを確認していきます。

---

*この記事は自動収集システムによって保存されました。*
