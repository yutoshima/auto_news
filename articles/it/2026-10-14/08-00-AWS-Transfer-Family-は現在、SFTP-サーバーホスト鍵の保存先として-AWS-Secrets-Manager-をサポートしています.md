---
title: "AWS Transfer Family は現在、SFTP サーバーホスト鍵の保存先として AWS Secrets Manager をサポートしています"
source: "AWS What's New"
category: "it"
published: 2026-10-14T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-secrets-host-keys/
---

# AWS Transfer Family は現在、SFTP サーバーホスト鍵の保存先として AWS Secrets Manager をサポートしています

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-secrets-host-keys/](https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-secrets-host-keys/)

## 概要

<p>AWS Transfer Family は現在、SFTP サーバーのホスト鍵をあなた自身の AWS アカウント内の AWS Secrets Manager に保存できるようになりました。これにより、サーバーの識別情報をより厳密に管理でき、サーバーの移行やフェイルオーバーをより簡素化できます。</p>
<p>従来、Transfer Family はホスト鍵をサービス内に保存していたため、関連する秘密鍵のマテリアルを取得することができませんでした。今回のリリースでは、サーバーを作成する際やホスト鍵をインポートする際に、保存先として Secrets Manager を選択できます。その後、秘密鍵のマテリアルを取得できます。</p>

---

*この記事は自動収集システムによって保存されました。*
