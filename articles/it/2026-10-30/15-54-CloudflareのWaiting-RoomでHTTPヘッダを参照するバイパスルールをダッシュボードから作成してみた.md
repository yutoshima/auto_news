---
title: "CloudflareのWaiting RoomでHTTPヘッダを参照するバイパスルールをダッシュボードから作成してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-30T15:54:46
url: https://dev.classmethod.jp/articles/cloudflare-waiting-room-http-request-headers-bypass-rule/
---

# CloudflareのWaiting RoomでHTTPヘッダを参照するバイパスルールをダッシュボードから作成してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月30日 15:54
- **URL**: [https://dev.classmethod.jp/articles/cloudflare-waiting-room-http-request-headers-bypass-rule/](https://dev.classmethod.jp/articles/cloudflare-waiting-room-http-request-headers-bypass-rule/)

## 概要

CloudflareのWaiting Roomで、あるHTTPリクエストヘッダが特定の値の場合に待合室をバイパスするルールを作成してみました。バイパスルール画面の式ビルダーでは作成できないのでカスタムルール画面で式を作成し、バイパスルール画面の式編集でその式を記載するのがポイントです。

---

*この記事は自動収集システムによって保存されました。*
