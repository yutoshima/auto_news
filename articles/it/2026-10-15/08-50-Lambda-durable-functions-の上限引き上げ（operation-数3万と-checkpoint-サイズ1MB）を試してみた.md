---
title: "Lambda durable functions の上限引き上げ（operation 数3万と checkpoint サイズ1MB）を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-15T08:50:02
url: https://dev.classmethod.jp/articles/aws-lambda-durable-functions-limit-increase/
---

# Lambda durable functions の上限引き上げ（operation 数3万と checkpoint サイズ1MB）を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 08:50
- **URL**: [https://dev.classmethod.jp/articles/aws-lambda-durable-functions-limit-increase/](https://dev.classmethod.jp/articles/aws-lambda-durable-functions-limit-increase/)

## 概要

AWS Lambda durable functions の上限が引き上げられ、operation 数は3,000から30,000に、checkpoint サイズは256 KBから1 MBになりました。どちらも旧上限を超える実行を試し、1つの durable execution のまま完了することを確かめました。

---

*この記事は自動収集システムによって保存されました。*
