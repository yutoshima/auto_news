---
title: "Azure StorageにPrivate Endpointを作っても公開アクセスは止まらない？VNetの内と外から読んで確かめた"
source: "DevelopersIO"
category: "it"
published: 2026-11-10T11:55:19
url: https://dev.classmethod.jp/articles/azure-storage-private-endpoint-public-access/
---

# Azure StorageにPrivate Endpointを作っても公開アクセスは止まらない？VNetの内と外から読んで確かめた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 11:55
- **URL**: [https://dev.classmethod.jp/articles/azure-storage-private-endpoint-public-access/](https://dev.classmethod.jp/articles/azure-storage-private-endpoint-public-access/)

## 概要

Azure StorageにPrivate Endpointを作り、VNet内のVMと手元のPCからBlobを読んで確かめました。作っただけでは公開経路から読め、外から拒否されたのは公開ネットワークアクセスを無効にした後でした。DNSと認可も含めて接続設計を整理します。

---

*この記事は自動収集システムによって保存されました。*
