---
title: "Claude Codeに同じバグを3回出すと、自動でルール化される話"
source: "Zenn"
category: "it"
published: 2026-06-29T02:00:09
url: https://zenn.dev/nexta_/articles/858e92ee22b4a4
---

# Claude Codeに同じバグを3回出すと、自動でルール化される話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月29日 02:00
- **URL**: [https://zenn.dev/nexta_/articles/858e92ee22b4a4](https://zenn.dev/nexta_/articles/858e92ee22b4a4)

## 概要

こんにちは。製造業向けSaaSを開発しているエンジニアです。
AIエージェントを使い込むと、誰もが必ずぶつかる壁があります。「同じ失敗を、何度もAIに繰り返される」ことと、その対策で記録を増やすと今度は 「記憶が肥大化して、肝心なルールがノイズに埋もれる」ことです。
私はこの2つを、セッション履歴を 「一次資料」 として扱い、アジャイル開発のふりかえりのようにAI自身の振る舞いを少しずつルール化していく学習機構（cc-retrospective-learner）で解こうとしました。仕組み自体は大げさなものではなく、自分の .claude 環境で開発の区切りごとに /retrospecti...

---

*この記事は自動収集システムによって保存されました。*
