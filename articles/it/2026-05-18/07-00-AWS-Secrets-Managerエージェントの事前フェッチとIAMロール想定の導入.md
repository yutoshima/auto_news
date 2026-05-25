---
title: "AWS Secrets Managerエージェントの事前フェッチとIAMロール想定の導入"
source: "AWS What's New"
category: "it"
published: 2026-05-18T07:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/05/secrets-manager-agent-prefetch-and-role-assumption/
---

# AWS Secrets Managerエージェントの事前フェッチとIAMロール想定の導入

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年05月18日 07:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/05/secrets-manager-agent-prefetch-and-role-assumption/](https://aws.amazon.com/about-aws/whats-new/2026/05/secrets-manager-agent-prefetch-and-role-assumption/)

## 概要

AWS Secrets Manager Agentは、新たに2つの機能をサポートします：起動時の事前取得と、秘密を取得するためのIAMロールの引き受け。事前取得を使用すると、起動時に取得してキャッシュする秘密のリストやタグ値を指定でき、アプリケーションの起動遅延を削減し、BatchGetSecretValue APIを通じてコストを最適化します。IAMロールの引き受けを使用すると、事前取得の設定や秘密取得のHTTPリクエストにロールARNを渡すことができます。

---

*この記事は自動収集システムによって保存されました。*
