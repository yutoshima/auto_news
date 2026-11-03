---
title: "Amazon Data FirehoseのLambda変換で、失敗・破棄したレコードがどこへ行くのか確かめてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-02T09:20:43
url: https://dev.classmethod.jp/articles/202611-mitsuguchi-firehose-to-lambda-kensho/
---

# Amazon Data FirehoseのLambda変換で、失敗・破棄したレコードがどこへ行くのか確かめてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月02日 09:20
- **URL**: [https://dev.classmethod.jp/articles/202611-mitsuguchi-firehose-to-lambda-kensho/](https://dev.classmethod.jp/articles/202611-mitsuguchi-firehose-to-lambda-kensho/)

## 概要

Amazon Data FirehoseのLambda変換で、失敗したレコードがS3のどこに、どんな形で残るのかを実際に検証してみました。正常なレコード・破棄・処理失敗・例外の4パターンを意図的に作り分けて、CloudFormationで構築した環境で試します。

---

*この記事は自動収集システムによって保存されました。*
