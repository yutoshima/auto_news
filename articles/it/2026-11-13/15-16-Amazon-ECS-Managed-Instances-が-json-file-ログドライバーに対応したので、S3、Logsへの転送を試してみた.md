---
title: "Amazon ECS Managed Instances が json-file ログドライバーに対応したので、S3、Logsへの転送を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-13T15:16:43
url: https://dev.classmethod.jp/articles/ecs-daemon-json-file-logs/
---

# Amazon ECS Managed Instances が json-file ログドライバーに対応したので、S3、Logsへの転送を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月13日 15:16
- **URL**: [https://dev.classmethod.jp/articles/ecs-daemon-json-file-logs/](https://dev.classmethod.jp/articles/ecs-daemon-json-file-logs/)

## 概要

Amazon ECS Managed Instances の json-file ログドライバーと、Managed Daemons のログドライバーボリュームで、nginx のログを AWS 提供の Fluent Bit から S3 と CloudWatch Logs に送りました。プラグインの追加もカスタムイメージも要りませんでした。ログはコンテナ別のディレクトリに置かれ、runtimeId で区別できます。

---

*この記事は自動収集システムによって保存されました。*
