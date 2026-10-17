---
title: "Cloudflare GatewayのForwardアクションで、許可したトラフィックにWorkerを挟む"
source: "DevelopersIO"
category: "it"
published: 2026-10-17T03:48:13
url: https://dev.classmethod.jp/articles/cloudflare-gateway-forward-worker/
---

# Cloudflare GatewayのForwardアクションで、許可したトラフィックにWorkerを挟む

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 03:48
- **URL**: [https://dev.classmethod.jp/articles/cloudflare-gateway-forward-worker/](https://dev.classmethod.jp/articles/cloudflare-gateway-forward-worker/)

## 概要

public betaとなったCloudflare GatewayのForwardアクションを公式ドキュメントで整理し、試しました。handle()の引数と設定の流れに加え、Gatewayを通した通信でcontextに入る値やログでの見え方を確かめた結果をまとめます。

---

*この記事は自動収集システムによって保存されました。*
