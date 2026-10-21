---
title: "Windows PowerShell で aws ecr get-login-password | docker login が 400 Bad Request になる原因は BOM だった"
source: "DevelopersIO"
category: "it"
published: 2026-10-20T06:49:14
url: https://dev.classmethod.jp/articles/powershell-ecr-docker-login-400-bom/
---

# Windows PowerShell で aws ecr get-login-password | docker login が 400 Bad Request になる原因は BOM だった

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月20日 06:49
- **URL**: [https://dev.classmethod.jp/articles/powershell-ecr-docker-login-400-bom/](https://dev.classmethod.jp/articles/powershell-ecr-docker-login-400-bom/)

## 概要

Windows PowerShell のパイプで ECR にログインできない問題を調査したところ、パスワードの先頭に付く目に見えない BOM（3バイト）が犯人だったという話です。原因の切り分け方と、3つの対処法をまとめます。

---

*この記事は自動収集システムによって保存されました。*
