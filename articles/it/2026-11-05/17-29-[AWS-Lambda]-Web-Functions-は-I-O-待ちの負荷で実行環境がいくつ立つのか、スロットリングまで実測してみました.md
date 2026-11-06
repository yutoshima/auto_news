---
title: "[AWS Lambda] Web Functions は I/O 待ちの負荷で実行環境がいくつ立つのか、スロットリングまで実測してみました"
source: "DevelopersIO"
category: "it"
published: 2026-11-05T17:29:19
url: https://dev.classmethod.jp/articles/lambda-web-functions-scaling-throttling-io-bound/
---

# [AWS Lambda] Web Functions は I/O 待ちの負荷で実行環境がいくつ立つのか、スロットリングまで実測してみました

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 17:29
- **URL**: [https://dev.classmethod.jp/articles/lambda-web-functions-scaling-throttling-io-bound/](https://dev.classmethod.jp/articles/lambda-web-functions-scaling-throttling-io-bound/)

## 概要

AWS Lambda Web Functionsの実行環境スケーリングについて、I/O待ち主体の負荷で実測してみました。関数作成直後と暖めた後で環境数や429エラーの出方がどう変わるのか、maxEnvironmentsやrateLimitの上限に当たったときの挙動を確認してみた結果を共有させてください

---

*この記事は自動収集システムによって保存されました。*
