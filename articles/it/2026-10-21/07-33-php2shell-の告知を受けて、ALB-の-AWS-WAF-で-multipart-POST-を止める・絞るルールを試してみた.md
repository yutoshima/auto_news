---
title: "php2shell の告知を受けて、ALB の AWS WAF で multipart POST を止める・絞るルールを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-21T07:33:26
url: https://dev.classmethod.jp/articles/aws-waf-alb-block-multipart-post/
---

# php2shell の告知を受けて、ALB の AWS WAF で multipart POST を止める・絞るルールを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月21日 07:33
- **URL**: [https://dev.classmethod.jp/articles/aws-waf-alb-block-multipart-post/](https://dev.classmethod.jp/articles/aws-waf-alb-block-multipart-post/)

## 概要

ALB 配下の PHP アプリを想定して、AWS WAF で multipart/form-data の POST を止める・絞るルールを試しました。Content-Type の書き方を変えても止まること、レートベースのルールは上限を超えたあとも十数件から数十件通ることを確かめました。

---

*この記事は自動収集システムによって保存されました。*
