---
title: "AWSにデプロイせず、FastAPI製Lambdaのarm64実行をCIで検証する"
source: "Zenn"
category: "it"
published: 2026-10-24T16:07:43
url: https://zenn.dev/shingokumon/articles/4da5acb9697d56
---

# AWSにデプロイせず、FastAPI製Lambdaのarm64実行をCIで検証する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 16:07
- **URL**: [https://zenn.dev/shingokumon/articles/4da5acb9697d56](https://zenn.dev/shingokumon/articles/4da5acb9697d56)

## 概要

はじめに
FastAPIで開発している案件判定API「SUMI Job Engine」に、AWSへデプロイせずにLambda向けパッケージを検証するCIを追加しました。
今回確認したかったのは、「SAMでビルドできるか」の一歩先です。ビルドした成果物をarm64のLambda公式Pythonコンテナに読み込ませ、実際のハンドラーを呼び出せるかを確かめました。
この記事では、実プロジェクトで使った構成とコードの要点を紹介します。コードは既存アプリからの抜粋です。単独で動くサンプル一式ではないため、導入する場合はハンドラー、パス、環境変数を自分のアプリに合わせて置き換えてください。
!
...

---

*この記事は自動収集システムによって保存されました。*
