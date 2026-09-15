---
title: "AWS Lambda の90分タイムアウト検証"
source: "Zenn"
category: "it"
published: 2026-09-14T04:25:24
url: https://zenn.dev/aws_japan/articles/lambda-90-minutes-timeout
---

# AWS Lambda の90分タイムアウト検証

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月14日 04:25
- **URL**: [https://zenn.dev/aws_japan/articles/lambda-90-minutes-timeout](https://zenn.dev/aws_japan/articles/lambda-90-minutes-timeout)

## 概要

はじめに
おはようございます、加藤です。2026年9月、AWS Lambda の関数タイムアウトが従来の15分から最大90分（5,400秒）に拡張されました。ただし無条件ではなく、対象は次の2つの条件を両方満たす場合のみです。

Lambda Managed Instances (LMI) 上で動く関数であること
非同期呼び出し、または ESM（イベントソースマッピング）経由の呼び出しであること

同期呼び出しは従来どおり15分のままです。「ついに Lambda で90分動かせる」と飛びつく前に押さえるべき条件がいくつかあるので、CDK で検証環境を組んで実際に動かして確かめました。...

---

*この記事は自動収集システムによって保存されました。*
