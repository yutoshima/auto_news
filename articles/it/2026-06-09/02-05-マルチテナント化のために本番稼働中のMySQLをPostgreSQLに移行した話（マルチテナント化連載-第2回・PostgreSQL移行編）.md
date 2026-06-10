---
title: "マルチテナント化のために本番稼働中のMySQLをPostgreSQLに移行した話（マルチテナント化連載 第2回・PostgreSQL移行編）"
source: "Zenn"
category: "it"
published: 2026-06-09T02:05:10
url: https://zenn.dev/counterworks/articles/0eb98271af2991
---

# マルチテナント化のために本番稼働中のMySQLをPostgreSQLに移行した話（マルチテナント化連載 第2回・PostgreSQL移行編）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月09日 02:05
- **URL**: [https://zenn.dev/counterworks/articles/0eb98271af2991](https://zenn.dev/counterworks/articles/0eb98271af2991)

## 概要

はじめに
こんにちは。株式会社カウンターワークスにて、テックリードとして、リーシングのDXを実現するクラウド管理システム 「ショップカウンター エンタープライズ」（以下 SCE）を開発しております shim です。
前回の俯瞰編に続いて、いよいよ各論に入っていきます。今回は Phase 1: MySQL から PostgreSQL への完全移行 がテーマです。
前回も触れた通り、マルチテナント化の中で Row Level Security（以下 RLS）を二重防御の DB 層として採用することを決めたのですが、それを使うために避けられなかったのが 「本番稼働中のサービスを、MySQL...

---

*この記事は自動収集システムによって保存されました。*
