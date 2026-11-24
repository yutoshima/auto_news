---
title: "ECS Action Logs のログ記録対象が追加されたので、Fargate のタスクのイベントを確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-23T14:55:51
url: https://dev.classmethod.jp/articles/amazon-ecs-action-logs-task-events/
---

# ECS Action Logs のログ記録対象が追加されたので、Fargate のタスクのイベントを確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 14:55
- **URL**: [https://dev.classmethod.jp/articles/amazon-ecs-action-logs-task-events/](https://dev.classmethod.jp/articles/amazon-ecs-action-logs-task-events/)

## 概要

Amazon ECS Action Logs のタスクのイベントを Fargate で試しました。イメージ取得失敗、コンテナの異常終了、コンテナのヘルスチェック失敗はそれぞれ別のイベント名で記録され、異常終了では終了コードを detail.containers[].exitCode で確認できました。

---

*この記事は自動収集システムによって保存されました。*
