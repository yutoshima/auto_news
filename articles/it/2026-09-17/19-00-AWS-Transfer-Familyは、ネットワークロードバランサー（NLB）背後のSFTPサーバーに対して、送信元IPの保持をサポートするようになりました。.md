---
title: "AWS Transfer Familyは、ネットワークロードバランサー（NLB）背後のSFTPサーバーに対して、送信元IPの保持をサポートするようになりました。"
source: "AWS What's New"
category: "it"
published: 2026-09-17T19:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/
---

# AWS Transfer Familyは、ネットワークロードバランサー（NLB）背後のSFTPサーバーに対して、送信元IPの保持をサポートするようになりました。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月17日 19:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/](https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/)

## 概要

<p>AWS Transfer Familyは、VPC内のエンドポイントを使用するSFTPサーバーの前にネットワークロードバランサー（NLB）を配置した場合、Proxy Protocol v2（PPv2）を用いてクライアントの元のソースIPアドレスを保持します。これにより、自身のNLBを使用する際にも、IPベースの監査・アクセス制御・コンプライアンスのためにクライアントの元のIPを可視化したまま保持できます。</p>
<p>従来、NLBはクライアントの元のIPを自分のプライベートIPに置き換えていたため、Transfer FamilyのログとイベントはNLBのアドレスを記録していました。</p>

---

*この記事は自動収集システムによって保存されました。*
