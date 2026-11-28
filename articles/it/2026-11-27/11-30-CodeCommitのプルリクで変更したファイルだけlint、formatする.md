---
title: "CodeCommitのプルリクで変更したファイルだけlint、formatする"
source: "DevelopersIO"
category: "it"
published: 2026-11-27T11:30:04
url: https://dev.classmethod.jp/articles/codecommit-pr-lint-format-changed-files/
---

# CodeCommitのプルリクで変更したファイルだけlint、formatする

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月27日 11:30
- **URL**: [https://dev.classmethod.jp/articles/codecommit-pr-lint-format-changed-files/](https://dev.classmethod.jp/articles/codecommit-pr-lint-format-changed-files/)

## 概要

CodeCommitでプルリクエストを作成、更新した際に、EventBridgeとCodeBuildを使ってlinterとformatterを実行する仕組みを構築してみました。この記事では、変更したファイルのみを対象とする方法について紹介しています。

---

*この記事は自動収集システムによって保存されました。*
