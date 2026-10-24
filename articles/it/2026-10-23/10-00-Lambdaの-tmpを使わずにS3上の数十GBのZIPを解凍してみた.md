---
title: "Lambdaの/tmpを使わずにS3上の数十GBのZIPを解凍してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-23T10:00:10
url: https://dev.classmethod.jp/articles/lambda-unzip-s3-zip-larger-than-tmp/
---

# Lambdaの/tmpを使わずにS3上の数十GBのZIPを解凍してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 10:00
- **URL**: [https://dev.classmethod.jp/articles/lambda-unzip-s3-zip-larger-than-tmp/](https://dev.classmethod.jp/articles/lambda-unzip-s3-zip-larger-than-tmp/)

## 概要

Lambdaの/tmpを使わずに、S3上の数十GBのZIPを展開する方法を2つ試しました。無圧縮（STORED）ならUploadPartCopyでS3内コピーして10GiBが4.3秒、圧縮済み（DEFLATE）ならストリーミング展開で約70MiB/s。方式の選び方と実装をまとめています。

---

*この記事は自動収集システムによって保存されました。*
