---
title: "OpenAPIという間接的な型共有をやめてoRPCを導入した話"
source: "Zenn"
category: "it"
published: 2026-05-07T00:00:09
url: https://zenn.dev/dress_code/articles/9040b2e3532693
---

# OpenAPIという間接的な型共有をやめてoRPCを導入した話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月07日 00:00
- **URL**: [https://zenn.dev/dress_code/articles/9040b2e3532693](https://zenn.dev/dress_code/articles/9040b2e3532693)

## 概要

はじめに
Dress Code 株式会社のかわうそです。
今回は、フロントエンドとバックエンドの型共有に OpenAPI（コード生成）を使っていた構成から、oRPC を導入した話を紹介します。
!
この記事は「バックエンドの実装から OpenAPI スキーマを生成し、そこからフロントエンド用の型をコード生成する」という構成が前提です。OpenAPI 自体を否定するものではなく、コントラクトファーストで OpenAPI を正として運用するアプローチなど、OpenAPI の活用方法は他にもあります。


 技術スタック
この記事で登場する主な技術スタックです。



レイヤー
技術


...

---

*この記事は自動収集システムによって保存されました。*
