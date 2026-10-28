---
title: "Lambda 関数の呼び出し（Invoke）で TooManyRequestsException（429）が返りました。再試行しても二重に実行されませんか。"
source: "DevelopersIO"
category: "it"
published: 2026-10-27T13:57:31
url: https://dev.classmethod.jp/articles/tsnote-lambda-invoke-429-retry-idempotent/
---

# Lambda 関数の呼び出し（Invoke）で TooManyRequestsException（429）が返りました。再試行しても二重に実行されませんか。

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月27日 13:57
- **URL**: [https://dev.classmethod.jp/articles/tsnote-lambda-invoke-429-retry-idempotent/](https://dev.classmethod.jp/articles/tsnote-lambda-invoke-429-retry-idempotent/)

## 概要

Lambda の同期呼び出しで `TooManyRequestsException` エラーが発生したとき、再試行で関数が二重実行されるのかについて確認してみました。実際の検証結果をもとに、エラー時の適切な対応方法を紹介します。

---

*この記事は自動収集システムによって保存されました。*
