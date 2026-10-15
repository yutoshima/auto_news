---
title: "Lambda Web Functions の MultiRegion エンドポイントは遅延が最小のリージョンに届くのか試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-14T14:54:04
url: https://dev.classmethod.jp/articles/lambda-web-functions-multiregion-lowest-latency-region/
---

# Lambda Web Functions の MultiRegion エンドポイントは遅延が最小のリージョンに届くのか試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 14:54
- **URL**: [https://dev.classmethod.jp/articles/lambda-web-functions-multiregion-lowest-latency-region/](https://dev.classmethod.jp/articles/lambda-web-functions-multiregion-lowest-latency-region/)

## 概要

AWS Lambda Web Functions のグローバル URL が遅延が最小のリージョンに届くかを、Route 53 ヘルスチェッカーと CloudShell で測りました。測った地点のすべてで遅延が最小のリージョンが応答し、振り分けは DNS の応答で行われていました。

---

*この記事は自動収集システムによって保存されました。*
