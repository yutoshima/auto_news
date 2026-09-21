---
title: "AWS Transfer Family は、NLB（Network Load Balancer）の背後にある SFTP サーバーに対して、ソース IP の保持をサポートします。"
source: "AWS What's New"
category: "it"
published: 2026-09-17T19:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/
---

# AWS Transfer Family は、NLB（Network Load Balancer）の背後にある SFTP サーバーに対して、ソース IP の保持をサポートします。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月17日 19:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/](https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/)

## 概要

<p>AWS Transfer Familyは、VPC内のエンドポイントを使用するSFTPサーバーの前にNetwork Load Balancer（NLB）を配置した場合、Proxy Protocol v2（PPv2）を用いてクライアントの送信元IPアドレスを保持します。自分自身のNLBを使用することで、IPベースの監査、アクセス制御、コンプライアンスのためにクライアントの送信元IPを可視化したまま維持できます。</p> 
<p>以前は、NLBがクライアントの送信元IPを自分のプライベートIPアドレスに置き換えていたため、Transfer FamilyのログとイベントにはNLBのアドレスが記録されていました。</p>

---

*この記事は自動収集システムによって保存されました。*
