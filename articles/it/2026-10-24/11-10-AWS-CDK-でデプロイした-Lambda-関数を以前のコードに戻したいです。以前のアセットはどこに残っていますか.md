---
title: "AWS CDK でデプロイした Lambda 関数を以前のコードに戻したいです。以前のアセットはどこに残っていますか"
source: "DevelopersIO"
category: "it"
published: 2026-10-24T11:10:06
url: https://dev.classmethod.jp/articles/tsnote-cdk-lambda-rollback-asset-s3-cdk-gc/
---

# AWS CDK でデプロイした Lambda 関数を以前のコードに戻したいです。以前のアセットはどこに残っていますか

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 11:10
- **URL**: [https://dev.classmethod.jp/articles/tsnote-cdk-lambda-rollback-asset-s3-cdk-gc/](https://dev.classmethod.jp/articles/tsnote-cdk-lambda-rollback-asset-s3-cdk-gc/)

## 概要

AWS CDK で Lambda 関数をデプロイした後、コードに不具合が見つかった時の切り戻し方法について解説します。ブートストラップ S3 バケットにアセットがどう残るのか、`cdk gc` で削除される仕組み、そして素早く対応するための方法をまとめました。

---

*この記事は自動収集システムによって保存されました。*
