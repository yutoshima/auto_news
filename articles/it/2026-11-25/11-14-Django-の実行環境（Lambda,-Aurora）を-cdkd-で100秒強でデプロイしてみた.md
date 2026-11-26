---
title: "Django の実行環境（Lambda, Aurora）を cdkd で100秒強でデプロイしてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-25T11:14:52
url: https://dev.classmethod.jp/articles/lambda-web-functions-aurora-without-vpc/
---

# Django の実行環境（Lambda, Aurora）を cdkd で100秒強でデプロイしてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 11:14
- **URL**: [https://dev.classmethod.jp/articles/lambda-web-functions-aurora-without-vpc/](https://dev.classmethod.jp/articles/lambda-web-functions-aurora-without-vpc/)

## 概要

Django アプリを動かす Lambda Web Functions と Aurora PostgreSQL のエクスプレス構成をつなぎ、cdkd の初回デプロイを約1分45秒で完了しました。通常構成の Aurora と NAT Gateway を置いた VPC 構成では約9分でした。

---

*この記事は自動収集システムによって保存されました。*
