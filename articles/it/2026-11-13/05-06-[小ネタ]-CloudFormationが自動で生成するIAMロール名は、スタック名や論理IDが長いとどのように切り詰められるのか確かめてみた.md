---
title: "[小ネタ] CloudFormationが自動で生成するIAMロール名は、スタック名や論理IDが長いとどのように切り詰められるのか確かめてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-13T05:06:49
url: https://dev.classmethod.jp/articles/202611-cloudformation-iam-role-name-truncation/
---

# [小ネタ] CloudFormationが自動で生成するIAMロール名は、スタック名や論理IDが長いとどのように切り詰められるのか確かめてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月13日 05:06
- **URL**: [https://dev.classmethod.jp/articles/202611-cloudformation-iam-role-name-truncation/](https://dev.classmethod.jp/articles/202611-cloudformation-iam-role-name-truncation/)

## 概要

CloudFormationが自動で生成するIAMロール名は、スタック名や論理IDが長いと切り詰められます。それぞれ何文字が使用されるのかを確認しました。

---

*この記事は自動収集システムによって保存されました。*
