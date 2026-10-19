---
title: "AWS Transfer Family が SFTP サーバーのホストキー用ストレージとして AWS Secrets Manager をサポートしました"
source: "AWS What's New"
category: "it"
published: 2026-10-14T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-secrets-host-keys/
---

# AWS Transfer Family が SFTP サーバーのホストキー用ストレージとして AWS Secrets Manager をサポートしました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-secrets-host-keys/](https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-secrets-host-keys/)

## 概要

<p>AWS Transfer Familyは現在、SFTPサーバーのホストキーをご自身のAWSアカウントのAWS Secrets Managerに保存できるようになりました。これにより、サーバーのアイデンティティをより管理しやすくなり、サーバーの移行やフェイルオーバーの手間を簡素化できます。</p>
<p>これまではTransfer Familyがホストキーをサービス内に保存していたため、関連する秘密鍵の情報を取得できませんでした。今回のリリースでは、サーバーを作成する際またはホストキーをインポートする際に、ストレージタイプとしてSecrets Managerを選択できます。その後、秘密鍵の取得が可能になります。</p>

---

*この記事は自動収集システムによって保存されました。*
