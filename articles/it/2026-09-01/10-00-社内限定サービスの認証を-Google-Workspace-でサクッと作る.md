---
title: "社内限定サービスの認証を Google Workspace でサクッと作る"
source: "Zenn"
category: "it"
published: 2026-09-01T10:00:05
url: https://zenn.dev/dress_code/articles/6134e6bd5e46c6
---

# 社内限定サービスの認証を Google Workspace でサクッと作る

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月01日 10:00
- **URL**: [https://zenn.dev/dress_code/articles/6134e6bd5e46c6](https://zenn.dev/dress_code/articles/6134e6bd5e46c6)

## 概要

はじめに
Dress Code 株式会社でプロダクトエンジニアをしている@cottpanです。
社内向けの小さな Web サービスを作るとき、毎回考慮しなければいけないのが認証です。実現したいことは「社内の人だけが見られればいい」とシンプルですが、毎回認証の部分を実装するのは手間になる上、退職者のアカウントを消し忘れるなどの運用コストにもつながります。
今回、社内で HTML を共有するためのサービスを作る機会があり、認証は全部 Google Workspace に寄せて実装を行いました。
通常の認証に加え、「CI からも叩きたい」「エージェントに API 経由でアクセスを許可したい...

---

*この記事は自動収集システムによって保存されました。*
