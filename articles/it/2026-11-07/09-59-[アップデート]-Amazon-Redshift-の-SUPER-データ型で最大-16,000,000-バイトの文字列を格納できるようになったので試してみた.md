---
title: "[アップデート] Amazon Redshift の SUPER データ型で最大 16,000,000 バイトの文字列を格納できるようになったので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-07T09:59:50
url: https://dev.classmethod.jp/articles/20261107-amazon-redshift-expands-super-to-16-million-bytes/
---

# [アップデート] Amazon Redshift の SUPER データ型で最大 16,000,000 バイトの文字列を格納できるようになったので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月07日 09:59
- **URL**: [https://dev.classmethod.jp/articles/20261107-amazon-redshift-expands-super-to-16-million-bytes/](https://dev.classmethod.jp/articles/20261107-amazon-redshift-expands-super-to-16-million-bytes/)

## 概要

Amazon Redshift の SUPER データ型で個々の文字列を最大 16,000,000 バイトまで格納できるようになり、65,535 バイトを超える文字列を含む JSON を分割せずにロードできます。Redshift Serverless でパラメータを有効にし、COPY・LISTAGG・日本語の文字列での上限を試しました。

---

*この記事は自動収集システムによって保存されました。*
