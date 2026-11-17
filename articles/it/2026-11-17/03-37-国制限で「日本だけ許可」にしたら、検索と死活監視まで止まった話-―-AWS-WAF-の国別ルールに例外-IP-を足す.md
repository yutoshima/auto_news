---
title: "国制限で「日本だけ許可」にしたら、検索と死活監視まで止まった話 ― AWS WAF の国別ルールに例外 IP を足す"
source: "DevelopersIO"
category: "it"
published: 2026-11-17T03:37:10
url: https://dev.classmethod.jp/articles/aws-waf-geo-block-exclude-crawlers-healthchecks/
---

# 国制限で「日本だけ許可」にしたら、検索と死活監視まで止まった話 ― AWS WAF の国別ルールに例外 IP を足す

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月17日 03:37
- **URL**: [https://dev.classmethod.jp/articles/aws-waf-geo-block-exclude-crawlers-healthchecks/](https://dev.classmethod.jp/articles/aws-waf-geo-block-exclude-crawlers-healthchecks/)

## 概要

AWS WAF で国別ルールを設定すると、検索エンジンのクローラーや Route 53 のヘルスチェッカーまで止まってしまう問題に直面しました。この記事では、必要な海外 IP だけを例外にする具体的なルール構成と、公開リストから IP を自動更新する運用方法をご紹介します。

---

*この記事は自動収集システムによって保存されました。*
