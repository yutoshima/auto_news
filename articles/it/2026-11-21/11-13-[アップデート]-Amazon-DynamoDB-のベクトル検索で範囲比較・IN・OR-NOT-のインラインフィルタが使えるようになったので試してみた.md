---
title: "[アップデート] Amazon DynamoDB のベクトル検索で範囲比較・IN・OR/NOT のインラインフィルタが使えるようになったので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-21T11:13:48
url: https://dev.classmethod.jp/articles/20211121-amazon-dynamodb-vector-filters/
---

# [アップデート] Amazon DynamoDB のベクトル検索で範囲比較・IN・OR/NOT のインラインフィルタが使えるようになったので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月21日 11:13
- **URL**: [https://dev.classmethod.jp/articles/20211121-amazon-dynamodb-vector-filters/](https://dev.classmethod.jp/articles/20211121-amazon-dynamodb-vector-filters/)

## 概要

Amazon DynamoDB のベクトル検索で、インラインフィルタに範囲比較・IN・OR・NOT が追加されました。アプリ側で絞り込むと 0 件だった「価格 10000 以下」の類似検索が、インラインフィルタでは 5 件返りました。AWS CLI で各演算子の動作と制約を検証します。

---

*この記事は自動収集システムによって保存されました。*
