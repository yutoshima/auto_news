---
title: "OpenTelemetryでStep Functions越しにtraceparentを引き回し、複数Lambdaを一つのトレースにつなぐ"
source: "Zenn"
category: "it"
published: 2026-10-15T03:59:10
url: https://zenn.dev/boy_techblog/articles/connecting-trace-serverless
---

# OpenTelemetryでStep Functions越しにtraceparentを引き回し、複数Lambdaを一つのトレースにつなぐ

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 03:59
- **URL**: [https://zenn.dev/boy_techblog/articles/connecting-trace-serverless](https://zenn.dev/boy_techblog/articles/connecting-trace-serverless)

## 概要

はじめに
横浜銀行アジャイル開発チームのwatariです。
AWS上で、次のようなサーバーレスアプリケーションをOpenTelemetryで計装する機会がありました。
これまではAWS X-Ray SDKを利用してトレースを可視化していましたが、AWSがOpenTelemetryへの移行を推奨しています。
そのためOpenTelemetryを用いた計装をPoC（概念実証）として試しました。

テレメトリの送信先にはNew Relicを使用します。本稿ではOTLPによる直接送信の実装に焦点を当て、New Relicのエージェントとの比較は扱いません。
WebアプリケーションやLambd...

---

*この記事は自動収集システムによって保存されました。*
