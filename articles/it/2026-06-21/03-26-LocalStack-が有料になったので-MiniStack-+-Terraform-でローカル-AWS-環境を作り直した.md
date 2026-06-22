---
title: "LocalStack が有料になったので MiniStack + Terraform でローカル AWS 環境を作り直した"
source: "Zenn"
category: "it"
published: 2026-06-21T03:26:04
url: https://zenn.dev/kamegoro/articles/ef1ab1c9527f9d
---

# LocalStack が有料になったので MiniStack + Terraform でローカル AWS 環境を作り直した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月21日 03:26
- **URL**: [https://zenn.dev/kamegoro/articles/ef1ab1c9527f9d](https://zenn.dev/kamegoro/articles/ef1ab1c9527f9d)

## 概要

はじめに
個人開発で AWS のインフラを Terraform で管理していると、こういう悩みが出てきます。

「terraform apply のたびに実 AWS を使うのはコストが怖いし、壊すのも嫌だ。ローカルで試したい」

そこで従来は LocalStack を使うのが定番でした。ところが 2026 年 3 月、LocalStack は Community Edition を廃止し、最新版の利用にはアカウント登録と認証トークンが必須になりました。無料の Hobby プランも「非商用に限定」という制約つきです。
代わりになるものを探していたところ、MiniStack という OS...

---

*この記事は自動収集システムによって保存されました。*
