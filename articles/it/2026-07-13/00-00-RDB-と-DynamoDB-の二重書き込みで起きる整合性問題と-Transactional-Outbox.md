---
title: "RDB と DynamoDB の二重書き込みで起きる整合性問題と Transactional Outbox"
source: "Zenn"
category: "it"
published: 2026-07-13T00:00:19
url: https://zenn.dev/dress_code/articles/1646ef6e35df62
---

# RDB と DynamoDB の二重書き込みで起きる整合性問題と Transactional Outbox

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月13日 00:00
- **URL**: [https://zenn.dev/dress_code/articles/1646ef6e35df62](https://zenn.dev/dress_code/articles/1646ef6e35df62)

## 概要

はじめに
このブログは Dress Code Advent Calendar 2026/07 の 9 日目の記事です。
Dress Code 株式会社のかわうそです。
今回は、CRUD ベースで動いているサービスを Event Sourcing へ移していく過程で、Transactional Outbox パターンを入れた話をご紹介します。
移行前の状態を簡単に整理すると、

現在状態は RDB で CRUD 管理している
変更履歴は別に「変更前後の全体スナップショットを丸ごと JSON で保存する」履歴テーブル

アプリケーションが書き込む監査ログ方式
DB ログから変更を捕捉する...

---

*この記事は自動収集システムによって保存されました。*
