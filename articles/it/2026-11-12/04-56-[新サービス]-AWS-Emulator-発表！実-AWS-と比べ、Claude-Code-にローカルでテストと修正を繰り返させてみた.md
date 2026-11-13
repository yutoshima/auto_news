---
title: "[新サービス] AWS Emulator 発表！実 AWS と比べ、Claude Code にローカルでテストと修正を繰り返させてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-12T04:56:06
url: https://dev.classmethod.jp/articles/20261112-aws-emulator/
---

# [新サービス] AWS Emulator 発表！実 AWS と比べ、Claude Code にローカルでテストと修正を繰り返させてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月12日 04:56
- **URL**: [https://dev.classmethod.jp/articles/20261112-aws-emulator/](https://dev.classmethod.jp/articles/20261112-aws-emulator/)

## 概要

Werner Vogels 氏のブログにSwami Sivasubramanian 氏が寄稿した、AWS アカウントもデプロイも不要な AWS Emulator について試しました。DynamoDB と SQS の挙動は実 AWS と同じ結果になり、API は数ミリ秒で応答。Claude Code に仕様とテストを先に書かせ、エミュレーター上で pytest の実行と修正を繰り返させた手順も紹介します。

---

*この記事は自動収集システムによって保存されました。*
