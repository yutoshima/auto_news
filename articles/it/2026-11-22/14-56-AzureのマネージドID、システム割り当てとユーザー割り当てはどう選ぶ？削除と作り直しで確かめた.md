---
title: "AzureのマネージドID、システム割り当てとユーザー割り当てはどう選ぶ？削除と作り直しで確かめた"
source: "DevelopersIO"
category: "it"
published: 2026-11-22T14:56:21
url: https://dev.classmethod.jp/articles/azure-managed-identity-lifecycle-choice/
---

# AzureのマネージドID、システム割り当てとユーザー割り当てはどう選ぶ？削除と作り直しで確かめた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月22日 14:56
- **URL**: [https://dev.classmethod.jp/articles/azure-managed-identity-lifecycle-choice/](https://dev.classmethod.jp/articles/azure-managed-identity-lifecycle-choice/)

## 概要

AzureのマネージドIDを、作り直した後も同じIDを残すか、同じ権限を共有してよいかの2軸で比べます。実機では、システム割り当ては作り直すと別のIDになり、ユーザー割り当ては残りました。IDを消してもロールの割り当ては残り、「不明」と表示されました。

---

*この記事は自動収集システムによって保存されました。*
