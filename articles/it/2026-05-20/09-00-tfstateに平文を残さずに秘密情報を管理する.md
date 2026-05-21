---
title: "tfstateに平文を残さずに秘密情報を管理する"
source: "Zenn"
category: "it"
published: 2026-05-20T09:00:00
url: https://zenn.dev/dely_jp/articles/terraform-ephemeral-write-only-secrets
---

# tfstateに平文を残さずに秘密情報を管理する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月20日 09:00
- **URL**: [https://zenn.dev/dely_jp/articles/terraform-ephemeral-write-only-secrets](https://zenn.dev/dely_jp/articles/terraform-ephemeral-write-only-secrets)

## 概要

はじめに
クラシル社でSREをしているKaitoです。
弊社では開発環境を含む全ての環境でIaC (Terraform) を採用しており、秘密情報 (Secrets Manager, SSM Parameter Store など) については SOPS × KMS で管理しています。
従来の手法では、以下のようにリソースを設定することになります。
data "sops_file" "app" {
  source_file = "secrets/app.sops.yaml"
}

resource "aws_secretsmanager_secret_version" "app" {...}

---

*この記事は自動収集システムによって保存されました。*
