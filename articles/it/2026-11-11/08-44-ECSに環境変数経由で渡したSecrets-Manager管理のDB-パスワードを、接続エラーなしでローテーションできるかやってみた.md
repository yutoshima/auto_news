---
title: "ECSに環境変数経由で渡したSecrets Manager管理のDB パスワードを、接続エラーなしでローテーションできるかやってみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-11T08:44:45
url: https://dev.classmethod.jp/articles/myan-ecs-secrets-rotation-20261110/
---

# ECSに環境変数経由で渡したSecrets Manager管理のDB パスワードを、接続エラーなしでローテーションできるかやってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月11日 08:44
- **URL**: [https://dev.classmethod.jp/articles/myan-ecs-secrets-rotation-20261110/](https://dev.classmethod.jp/articles/myan-ecs-secrets-rotation-20261110/)

## 概要

Secrets Manager のローテーションをきっかけに ECS on Fargate のサービスを自動で再デプロイする構成を作り、シングルユーザー方式と交代ユーザー方式で、ローテーション中のリクエストがどうなるかを比べてみました。

---

*この記事は自動収集システムによって保存されました。*
