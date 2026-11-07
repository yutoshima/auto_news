---
title: "AD Connector の DNS 変更後、Amazon WorkSpaces（Windows）を再構築せずに新しい DNS へ切り替える方法"
source: "DevelopersIO"
category: "it"
published: 2026-11-06T06:34:33
url: https://dev.classmethod.jp/articles/tsnote-aws-workspaces-directoryservice-adconnector-dns-Content/
---

# AD Connector の DNS 変更後、Amazon WorkSpaces（Windows）を再構築せずに新しい DNS へ切り替える方法

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月06日 06:34
- **URL**: [https://dev.classmethod.jp/articles/tsnote-aws-workspaces-directoryservice-adconnector-dns-Content/](https://dev.classmethod.jp/articles/tsnote-aws-workspaces-directoryservice-adconnector-dns-Content/)

## 概要

ActiveDirectoryのリプレースに伴いDNS IPが変わる場合、Amazon WorkSpacesのレジストリにある旧DNS設定を新しいものに更新する必要があります。本記事では、既存WorkSpaceを再構築せずにPowerShellでレジストリを直接更新し、段階的にDNSを切り替える手順をご紹介します。

---

*この記事は自動収集システムによって保存されました。*
