---
title: "CloudWatch Logs のアカウントレベル保持期間ポリシーを、個別設定済みのロググループに適用してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-12T04:40:48
url: https://dev.classmethod.jp/articles/cloudwatch-logs-account-level-retention-policy/
---

# CloudWatch Logs のアカウントレベル保持期間ポリシーを、個別設定済みのロググループに適用してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月12日 04:40
- **URL**: [https://dev.classmethod.jp/articles/cloudwatch-logs-account-level-retention-policy/](https://dev.classmethod.jp/articles/cloudwatch-logs-account-level-retention-policy/)

## 概要

Amazon CloudWatch Logs のアカウントレベル保持期間ポリシーを、保持期間を個別設定したロググループへ RETROACTIVE で適用しました。個別設定が7日でも365日でもポリシーの値に置き換わり、プレフィックスが重なるロググループには長い方が適用されました。

---

*この記事は自動収集システムによって保存されました。*
