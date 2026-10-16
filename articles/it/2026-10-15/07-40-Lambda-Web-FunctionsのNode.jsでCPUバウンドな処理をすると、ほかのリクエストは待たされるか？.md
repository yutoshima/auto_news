---
title: "Lambda Web FunctionsのNode.jsでCPUバウンドな処理をすると、ほかのリクエストは待たされるか？"
source: "DevelopersIO"
category: "it"
published: 2026-10-15T07:40:20
url: https://dev.classmethod.jp/articles/shuntaka-lambda-web-functions-nodejs-cpu-bound/
---

# Lambda Web FunctionsのNode.jsでCPUバウンドな処理をすると、ほかのリクエストは待たされるか？

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 07:40
- **URL**: [https://dev.classmethod.jp/articles/shuntaka-lambda-web-functions-nodejs-cpu-bound/](https://dev.classmethod.jp/articles/shuntaka-lambda-web-functions-nodejs-cpu-bound/)

## 概要

Lambda Web Functions で CPU バウンドなリクエストが同時実行されたとき、本当にほかのリクエストを止めるのか、実際に測定して確かめました。結果は、空いている環境があれば Lambda は処理中の環境を避けます。どの環境も処理中なら Node.js は待たされ、Go は待たされない、各言語の機構通り動作するという結果でした。

---

*この記事は自動収集システムによって保存されました。*
