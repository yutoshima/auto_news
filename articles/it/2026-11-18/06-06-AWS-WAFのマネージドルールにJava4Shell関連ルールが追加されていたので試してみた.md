---
title: "AWS WAFのマネージドルールにJava4Shell関連ルールが追加されていたので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-18T06:06:12
url: https://dev.classmethod.jp/articles/aws-waf-known-bad-inputs-java4shell/
---

# AWS WAFのマネージドルールにJava4Shell関連ルールが追加されていたので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月18日 06:06
- **URL**: [https://dev.classmethod.jp/articles/aws-waf-known-bad-inputs-java4shell/](https://dev.classmethod.jp/articles/aws-waf-known-bad-inputs-java4shell/)

## 概要

AWS WAF のマネージドルール AWSManagedRulesKnownBadInputsRuleSet（Version_1.28）に追加された Java4Shell 向けの 3 ルールを固定応答の ALB で確かめました。テストスクリプトで、リクエストヘッダーに含まれる攻撃コードが検出されることを確認できました。

---

*この記事は自動収集システムによって保存されました。*
