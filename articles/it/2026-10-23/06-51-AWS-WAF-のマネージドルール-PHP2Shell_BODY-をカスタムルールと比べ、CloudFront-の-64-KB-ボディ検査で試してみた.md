---
title: "AWS WAF のマネージドルール PHP2Shell_BODY をカスタムルールと比べ、CloudFront の 64 KB ボディ検査で試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-23T06:51:33
url: https://dev.classmethod.jp/articles/aws-waf-php2shell-body-managed-rule/
---

# AWS WAF のマネージドルール PHP2Shell_BODY をカスタムルールと比べ、CloudFront の 64 KB ボディ検査で試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 06:51
- **URL**: [https://dev.classmethod.jp/articles/aws-waf-php2shell-body-managed-rule/](https://dev.classmethod.jp/articles/aws-waf-php2shell-body-managed-rule/)

## 概要

AWS WAF のマネージドルール PHP2Shell_BODY は、カスタムルール PHP2Shell と同じリクエストを止めました。CloudFront でボディ検査上限を 64 KB にすると、ALB で検査できなかった 8 KB より後ろの文字列も、上限の位置までサイズルールなしで検出しました。

---

*この記事は自動収集システムによって保存されました。*
