---
title: "AWS Elastic Disaster Recoveryは現在、LinuxサーバーのUEFI起動モードを保持します"
source: "AWS What's New"
category: "it"
published: 2026-08-10T13:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/08/aws-drs-linux-uefi
---

# AWS Elastic Disaster Recoveryは現在、LinuxサーバーのUEFI起動モードを保持します

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年08月10日 13:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/08/aws-drs-linux-uefi](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-drs-linux-uefi)

## 概要

AWS Elastic Disaster Recovery（AWS DRS）は、UEFIファームウェアで起動するLinuxソースサーバを復旧する際に、UEFIブートモードを維持します。これまではDRSがこれらのLinuxサーバをレガシーBIOSモードで起動していたため、復旧後に追加の設定が必要になることがありました。現在は、復旧したLinuxインスタンスがソースサーバと同じUEFIブートモードで起動します。つまり、復旧インスタンスがソース環境とより近い状態で動作するため、UEFIブート挙動に依存するアプリケーションが正確に戻ってくることになります。

---

*この記事は自動収集システムによって保存されました。*
