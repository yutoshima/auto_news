---
title: "AWSでWebリクエストを受ける8パターンと「オリジンを裸にしない」設定プラクティス"
source: "はてブ テクノロジー"
category: "it"
published: 2026-11-06T23:36:13
url: https://zenn.dev/anfangd/articles/aws-web-ingress-origin-protection
---

# AWSでWebリクエストを受ける8パターンと「オリジンを裸にしない」設定プラクティス

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年11月06日 23:36
- **URL**: [https://zenn.dev/anfangd/articles/aws-web-ingress-origin-protection](https://zenn.dev/anfangd/articles/aws-web-ingress-origin-protection)

## 概要

この記事は、Claude と一緒に AWS 公式ドキュメントを調べ、構成図を作りながら整理した内容をまとめたものです。各設定の根拠は、記事中のリンク先の公式ドキュメントで確認できます。 はじめに 先日、X（旧Twitter）でこんな趣旨の話題が流れてきました。 CloudFront + WAF → ALB の構成では、ALB の SG に CloudFront...

---

*この記事は自動収集システムによって保存されました。*
