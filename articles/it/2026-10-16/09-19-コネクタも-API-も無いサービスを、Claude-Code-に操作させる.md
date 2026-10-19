---
title: "コネクタも API も無いサービスを、Claude Code に操作させる"
source: "Zenn"
category: "it"
published: 2026-10-16T09:19:08
url: https://zenn.dev/edash_tech_blog/articles/6250fc61ccf009
---

# コネクタも API も無いサービスを、Claude Code に操作させる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月16日 09:19
- **URL**: [https://zenn.dev/edash_tech_blog/articles/6250fc61ccf009](https://zenn.dev/edash_tech_blog/articles/6250fc61ccf009)

## 概要

こんにちは、e-dash の中島です。
SRE として認証基盤やインフラを見ています。
Claude Code から外部サービスを操作するときは、MCP のコネクタを使います。
Notion や GitHub のように広く使われているサービスなら、だいたい用意されています。
自動化を進めていくと、コネクタも API も無いサービスがどうしても残ります。
業務に合わせて選んだ小さな SaaS や、社内向けの管理コンソールです。
設定を変えるにも状態を見るにも、人が画面を開くしかありません。
Claude Code に Chrome 拡張をつなぐと、ここに入口ができます。
画面をそのまま読ま...

---

*この記事は自動収集システムによって保存されました。*
