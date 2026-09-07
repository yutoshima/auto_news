---
title: "GitHub の権限管理を Terraform 化すると体験がよかった"
source: "Zenn"
category: "it"
published: 2026-09-06T11:50:58
url: https://zenn.dev/dev_commune/articles/github-terraform-permission-management
---

# GitHub の権限管理を Terraform 化すると体験がよかった

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月06日 11:50
- **URL**: [https://zenn.dev/dev_commune/articles/github-terraform-permission-management](https://zenn.dev/dev_commune/articles/github-terraform-permission-management)

## 概要

はじめに
新規のメンバーが入るたび、チームの構成が変わるたび、依頼が Slack ワークフローで流れてきます。その都度、GitHub をブラウザで開いてパスキーで認証して、画面をポチポチする。しんどいですね。
いい加減 Terraform にしました。なにを管理したかと詰まったところについて紹介します。
https://github.com/integrations/terraform-provider-github

 管理したもの
Terraform でこれらを管理することにしました。すべてを管理するわけではありません。まずは画面ポチポチを減らすこと、依頼自体を Pull Req...

---

*この記事は自動収集システムによって保存されました。*
