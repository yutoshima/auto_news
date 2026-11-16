---
title: "Amazon S3のアクセス許可は、複数のAWSアカウントにまたがる付与の一覧表示をサポートするようになりました"
source: "AWS What's New"
category: "it"
published: 2026-11-10T14:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-access-grants-list-across-regions/
---

# Amazon S3のアクセス許可は、複数のAWSアカウントにまたがる付与の一覧表示をサポートするようになりました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 14:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-access-grants-list-across-regions/](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-access-grants-list-across-regions/)

## 概要

<p>Amazon S3 アクセス許可は、複数の AWS アカウントにまたがるすべての許可を、1 回の API 呼び出しで検出・一覧表示できるようになりました。これにより、各アカウントを個別に照会する必要がなくなります。1 回の <i>ListCallerAccessGrants</i> 呼び出しで、あなた自身の S3 アクセス許可インスタンスからの許可と、共有されているすべてのインスタンスの許可を返し、アクセス可能な S3 データの全体像を把握できます。</p> 
<p>新しい <i>InstanceScope</i> パラメータを <i>ALL</i> に設定して <i>ListCallerAccessGrants</i> リクエストを送ると、S3 アクセス許可は</p>

---

*この記事は自動収集システムによって保存されました。*
