---
title: "/claude-api prompt-audit で棚卸ししたら、Claude Opus 5.5 化で外れた設定がぞろぞろ出てきた"
source: "Zenn"
category: "it"
published: 2026-09-25T01:59:47
url: https://zenn.dev/nanora/articles/20260925-claude-prompt-audit-opus55
---

# /claude-api prompt-audit で棚卸ししたら、Claude Opus 5.5 化で外れた設定がぞろぞろ出てきた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月25日 01:59
- **URL**: [https://zenn.dev/nanora/articles/20260925-claude-prompt-audit-opus55](https://zenn.dev/nanora/articles/20260925-claude-prompt-audit-opus55)

## 概要

TL;DR

Claude Code 同梱の /claude-api prompt-audit で、CLAUDE.md やプロンプトの古い書き方を洗い出せる
自前のエージェントに当てたら、言い回しより「書いてあることと実物のずれ」がぞろぞろ出た

opus がいつの間にか Opus 5.5 になっていて、effort 設定も効かず重い xhigh のままだった
effort が効いているかは起動ログに出ない。セッション記録を見るしかない
指示を消すなら、消した版と挙動を比べてから。1 つは消すと明確に悪化した



X で「/claude-api prompt-audit と打てば、s...

---

*この記事は自動収集システムによって保存されました。*
