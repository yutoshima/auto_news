---
title: "Global Accelerator が TLS リスナーの NLB でもクライアント IP を保持するようになったので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-24T16:31:54
url: https://dev.classmethod.jp/articles/global-accelerator-client-ip-nlb-tls/
---

# Global Accelerator が TLS リスナーの NLB でもクライアント IP を保持するようになったので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月24日 16:31
- **URL**: [https://dev.classmethod.jp/articles/global-accelerator-client-ip-nlb-tls/](https://dev.classmethod.jp/articles/global-accelerator-client-ip-nlb-tls/)

## 概要

TLS リスナーを持つ NLB を、クライアント IP アドレスを保持する AWS Global Accelerator のエンドポイントに追加して試しました。ターゲットで見える送信元 IP は元のクライアント IP アドレスで、ターゲットのセキュリティグループのソースとしても利用できました。

---

*この記事は自動収集システムによって保存されました。*
