---
title: "日本語の個人情報を Bedrock Guardrails, SDP, Presidio でマスキングして比較する"
source: "Zenn"
category: "it"
published: 2026-10-17T23:00:05
url: https://zenn.dev/fusic/articles/a77ba348115364
---

# 日本語の個人情報を Bedrock Guardrails, SDP, Presidio でマスキングして比較する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 23:00
- **URL**: [https://zenn.dev/fusic/articles/a77ba348115364](https://zenn.dev/fusic/articles/a77ba348115364)

## 概要

はじめに
こんにちは、Fusicの大宮です。
問い合わせメールや通話記録を外部に渡したり、生成AIで分析したりする前には、個人情報を消したい（マスキングしたい）、という場面があるかと思います。
ただ、日本語の文章には、全角の数字や和暦、話し言葉など、英語にはない書き方が多くあります。
2026年10月、クラウドのサービスとオープンソースのツールで、日本語の個人情報をどこまでマスキングできるのか気になり、試しました!
比べたのは次の3つです。


Sensitive Data Protection（Google Cloud。以下 SDP）

Amazon Bedrock Guardra...

---

*この記事は自動収集システムによって保存されました。*
