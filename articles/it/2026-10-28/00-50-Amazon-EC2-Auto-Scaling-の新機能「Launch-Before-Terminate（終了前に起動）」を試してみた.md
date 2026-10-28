---
title: "Amazon EC2 Auto Scaling の新機能「Launch Before Terminate（終了前に起動）」を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-28T00:50:10
url: https://dev.classmethod.jp/articles/asg-launch-before-terminate-account-setting/
---

# Amazon EC2 Auto Scaling の新機能「Launch Before Terminate（終了前に起動）」を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 00:50
- **URL**: [https://dev.classmethod.jp/articles/asg-launch-before-terminate-account-setting/](https://dev.classmethod.jp/articles/asg-launch-before-terminate-account-setting/)

## 概要

Amazon EC2 Auto Scaling の Launch Before Terminate をアカウント単位で有効にし、リフレッシュ中の台数を確認しました。指定なしのリフレッシュでは、新しいインスタンスが healthy になってから旧インスタンスが終了し、healthy ターゲットは4台を下回りませんでした。

---

*この記事は自動収集システムによって保存されました。*
