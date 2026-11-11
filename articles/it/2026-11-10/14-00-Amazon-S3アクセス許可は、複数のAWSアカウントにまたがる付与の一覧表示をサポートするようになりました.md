---
title: "Amazon S3アクセス許可は、複数のAWSアカウントにまたがる付与の一覧表示をサポートするようになりました"
source: "AWS What's New"
category: "it"
published: 2026-11-10T14:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-access-grants-list-across-regions/
---

# Amazon S3アクセス許可は、複数のAWSアカウントにまたがる付与の一覧表示をサポートするようになりました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 14:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-access-grants-list-across-regions/](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-access-grants-list-across-regions/)

## 概要

<p>Amazon S3 アクセス権限の取得機能は、単一の API 呼び出しで複数の AWS アカウントにまたがるすべての権限を検出・一覧表示できるようになり、アカウントごとにクエリを実行する必要がなくなりました。単一の <i>ListCallerAccessGrants</i> 呼び出しで、自分自身の S3 アクセス権限インスタンスと、あなたと共有されているすべてのインスタンスから権限を返し、アクセス可能な S3 データの全体像を提供します。</p> 
<p>新しい <i>InstanceScope</i> パラメータを <i>ALL</i> に設定して <i>ListCallerAccessGrants</i> リクエストを送ると、S3 アクセス権限の取得機能は、あなたがアクセスできるすべての権限を返します。</p>

---

*この記事は自動収集システムによって保存されました。*
