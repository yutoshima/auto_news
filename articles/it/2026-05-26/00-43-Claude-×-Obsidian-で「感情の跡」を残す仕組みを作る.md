---
title: "Claude × Obsidian で「感情の跡」を残す仕組みを作る"
source: "Zenn"
category: "it"
published: 2026-05-26T00:43:00
url: https://zenn.dev/miyaken0805/articles/ed70d88fa81c34
---

# Claude × Obsidian で「感情の跡」を残す仕組みを作る

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月26日 00:43
- **URL**: [https://zenn.dev/miyaken0805/articles/ed70d88fa81c34](https://zenn.dev/miyaken0805/articles/ed70d88fa81c34)

## 概要

はじめに
AIと会話していると、すごくいいアイデアが出たり、深い内省ができたりすることがある。でも、チャットが終わるとその内容は流れていく。「あの時Claudeと話した内容、なんだったっけ…」を何度か繰り返して、ようやく気づいた、考えた跡を残す仕組みの必要性。
この記事では、Claude（claude.ai）とObsidianをMCP経由で接続し、会話から生まれたアイデアやジャーナリングの記録を構造化して保存する仕組みの構築過程を紹介する。
最終的にはClaude.aiのカスタムスキルとして /obsidian ideas と打つだけで保存できるところまで。

 この記事で扱うこと
...

---

*この記事は自動収集システムによって保存されました。*
