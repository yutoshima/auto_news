---
title: "集約したCloudWatch Alarmの通知に発生元のアカウントIDを出すなら、Step Functionsで取り出そう"
source: "DevelopersIO"
category: "it"
published: 2026-11-28T01:15:36
url: https://dev.classmethod.jp/articles/centralized-cloudwatch-alarm-notification-source-account-id/
---

# 集約したCloudWatch Alarmの通知に発生元のアカウントIDを出すなら、Step Functionsで取り出そう

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月28日 01:15
- **URL**: [https://dev.classmethod.jp/articles/centralized-cloudwatch-alarm-notification-source-account-id/](https://dev.classmethod.jp/articles/centralized-cloudwatch-alarm-notification-source-account-id/)

## 概要

集約したCloudWatch Alarmの通知に発生元のアカウントIDを出そうとしたところ、EventBridgeのInput Transformerでは取り出せませんでした。取り出せなかった理由と、代わりにStep Functionsで取り出してから通知に渡す構成をまとめます。

---

*この記事は自動収集システムによって保存されました。*
