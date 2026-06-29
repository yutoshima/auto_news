---
title: "ECS のデプロイを ecspresso へ移行して自動化した話"
source: "Zenn"
category: "it"
published: 2026-06-29T03:43:53
url: https://zenn.dev/lincwell_inc/articles/c60c337017aa49
---

# ECS のデプロイを ecspresso へ移行して自動化した話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月29日 03:43
- **URL**: [https://zenn.dev/lincwell_inc/articles/c60c337017aa49](https://zenn.dev/lincwell_inc/articles/c60c337017aa49)

## 概要

はじめに
こんにちは。Linc'well R&amp;S（Reliability &amp; Security）チームのくのです！
弊社では複数のサービスを ECS（Fargate）上で運用しているのですが、今回はそのうちの一つを対象に、デプロイの自動化に取り組みました。
これまでこのサービスのデプロイは、ECR にイメージを push し、手動で ECS サービスを更新する、という手作業で行っていました。ECS のタスク定義・サービス自体は Terraform で管理していましたが、イメージタグを :latest で運用していたため、デプロイのたびにタスク定義の中身を書き換える必要...

---

*この記事は自動収集システムによって保存されました。*
