---
title: "Claude Code の使用量はどう数えられているのか ── Max 20x で実測した重みは API 料金表と違った"
source: "Zenn"
category: "it"
published: 2026-10-01T02:34:27
url: https://zenn.dev/tksfjt1024/articles/25c0ab111c277c
---

# Claude Code の使用量はどう数えられているのか ── Max 20x で実測した重みは API 料金表と違った

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月01日 02:34
- **URL**: [https://zenn.dev/tksfjt1024/articles/25c0ab111c277c](https://zenn.dev/tksfjt1024/articles/25c0ab111c277c)

## 概要

Claude Code を Pro や Max のプランで使うと、使った分だけ「使用量制限」の枠を消費します。この制限には、5 時間ごとにリセットされる「5時間のセッション制限」と、週ごとにリセットされる「週間使用制限」の 2 つがあります[1]。この 5 時間枠と週間枠が何でどれだけ減るのかを、条件を揃えた実験で測り、使用量の計算式を求めました。
主な結果は次のとおりです。

cache read（キャッシュから読み直す分）も使用量に入ります。ただし、1 トークンの重みは input の 1/40（0.025 倍）です。
headless（claude -p や Agent SDK か...

---

*この記事は自動収集システムによって保存されました。*
