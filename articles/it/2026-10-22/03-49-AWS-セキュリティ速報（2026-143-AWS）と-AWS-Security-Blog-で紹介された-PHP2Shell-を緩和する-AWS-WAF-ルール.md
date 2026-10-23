---
title: "AWS セキュリティ速報（2026-143-AWS）と AWS Security Blog で紹介された PHP2Shell を緩和する AWS WAF ルールを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-22T03:49:43
url: https://dev.classmethod.jp/articles/aws-security-bulletin-php2shell-waf-rules/
---

# AWS セキュリティ速報（2026-143-AWS）と AWS Security Blog で紹介された PHP2Shell を緩和する AWS WAF ルールを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 03:49
- **URL**: [https://dev.classmethod.jp/articles/aws-security-bulletin-php2shell-waf-rules/](https://dev.classmethod.jp/articles/aws-security-bulletin-php2shell-waf-rules/)

## 概要

PHP2Shell（CVE-2026-109618、CVE-2026-109619）を緩和する 2 つのルール（PHP2Shell と Block-Oversize-Body）を AWS WAF に入れ、止まる・通るリクエストを curl で確かめ、正当なリクエストが止まる副作用も確認しました。

---

*この記事は自動収集システムによって保存されました。*
