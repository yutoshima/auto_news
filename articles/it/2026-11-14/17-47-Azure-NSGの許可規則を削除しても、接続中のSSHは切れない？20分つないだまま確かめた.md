---
title: "Azure NSGの許可規則を削除しても、接続中のSSHは切れない？20分つないだまま確かめた"
source: "DevelopersIO"
category: "it"
published: 2026-11-14T17:47:18
url: https://dev.classmethod.jp/articles/azure-nsg-existing-connections/
---

# Azure NSGの許可規則を削除しても、接続中のSSHは切れない？20分つないだまま確かめた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月14日 17:47
- **URL**: [https://dev.classmethod.jp/articles/azure-nsg-existing-connections/](https://dev.classmethod.jp/articles/azure-nsg-existing-connections/)

## 概要

Azure NSGでSSHの許可規則を削除し、接続中のセッションと新しい接続がどうなるかを実機で確かめました。既存のセッションはループが終わって閉じるまでの約20分間切れず、新しい接続はタイムアウトしました。規則変更後の確認観点とflushConnectionの現状も整理します。

---

*この記事は自動収集システムによって保存されました。*
