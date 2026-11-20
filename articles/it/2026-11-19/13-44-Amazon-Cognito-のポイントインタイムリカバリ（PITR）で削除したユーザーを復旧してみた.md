---
title: "Amazon Cognito のポイントインタイムリカバリ（PITR）で削除したユーザーを復旧してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T13:44:10
url: https://dev.classmethod.jp/articles/amazon-cognito-point-in-time-recovery/
---

# Amazon Cognito のポイントインタイムリカバリ（PITR）で削除したユーザーを復旧してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 13:44
- **URL**: [https://dev.classmethod.jp/articles/amazon-cognito-point-in-time-recovery/](https://dev.classmethod.jp/articles/amazon-cognito-point-in-time-recovery/)

## 概要

Amazon Cognito のポイントインタイムリカバリ（PITR）で、削除したユーザーを復旧しました。削除したユーザーは sub、パスワード、グループ所属、TOTP MFA が元のまま戻り、復旧ポイント後に作ったユーザーは削除されました。確認中は書き込みが拒否されました。

---

*この記事は自動収集システムによって保存されました。*
