---
title: "Bedrock の Structured outputs が Claude 全モデルでサポート、最新 Haiku 5.5 で試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-21T01:28:33
url: https://dev.classmethod.jp/articles/bedrock-claude-haiku55-structured-outputs/
---

# Bedrock の Structured outputs が Claude 全モデルでサポート、最新 Haiku 5.5 で試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月21日 01:28
- **URL**: [https://dev.classmethod.jp/articles/bedrock-claude-haiku55-structured-outputs/](https://dev.classmethod.jp/articles/bedrock-claude-haiku55-structured-outputs/)

## 概要

Amazon Bedrock の Structured outputs を Claude Haiku 5.5 で検証しました。InvokeModel、Converse、strict tool use のいずれもスキーマ通りの JSON が返り、JP と global の結果は同じでした。応答の先頭が thinking ブロックになる場合があるため、JSON は text ブロックから取り出す必要がありました。

---

*この記事は自動収集システムによって保存されました。*
