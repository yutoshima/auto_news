---
title: "1 行渡すと Claude Code が 1 時間自走する ─ E2E テスト駆動で新機能を作らせた話"
source: "Zenn"
category: "it"
published: 2026-05-28T01:01:10
url: https://zenn.dev/canly/articles/c7da70a520d1b8
---

# 1 行渡すと Claude Code が 1 時間自走する ─ E2E テスト駆動で新機能を作らせた話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月28日 01:01
- **URL**: [https://zenn.dev/canly/articles/c7da70a520d1b8](https://zenn.dev/canly/articles/c7da70a520d1b8)

## 概要

はじめに
私たちのチームは Slack 上で動く社内向け AI エージェントを開発・運用しています。新機能追加のたびに「Claude Code が実装したと言うが実際に Slack で動かない」という事象にあたっていたので、Claude Code に E2E テストケース 1 行を渡せば計画から実装・デプロイ・検証まで自走する仕組み を /e2e-dev というスラッシュコマンドとして作りました。1 回の依頼で 1 時間自走することもあり、その間 人間は別作業に集中できます（最後の Slack 目視確認は残ります）。

 何を作っているか
Slack で @bot にメンションして自...

---

*この記事は自動収集システムによって保存されました。*
