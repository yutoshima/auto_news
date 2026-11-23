---
title: "Azure Service Busの重複検出で二重処理は防げる？同じMessageIdの再送と再配信を試した"
source: "DevelopersIO"
category: "it"
published: 2026-11-22T14:58:30
url: https://dev.classmethod.jp/articles/azure-service-bus-duplicate-boundaries/
---

# Azure Service Busの重複検出で二重処理は防げる？同じMessageIdの再送と再配信を試した

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月22日 14:58
- **URL**: [https://dev.classmethod.jp/articles/azure-service-bus-duplicate-boundaries/](https://dev.classmethod.jp/articles/azure-service-bus-duplicate-boundaries/)

## 概要

Azure Service Busの重複検出を実機で試しました。同じMessageIdで再送したメッセージは、送信が成功しても捨てられ、1件目の受信後でも時間窓の中なら同じでした。一方、完了を通知する前に受信をやめると同じメッセージが再配信されました。

---

*この記事は自動収集システムによって保存されました。*
