---
title: "ClaudeにiOSシミュレーターのスクリーンショットを読ませるのをやめて、操作で増えるコンテキストを43%削減した"
source: "Zenn"
category: "it"
published: 2026-10-18T02:56:18
url: https://zenn.dev/eai/articles/dont-let-agents-see-the-ios-sim-screen
---

# ClaudeにiOSシミュレーターのスクリーンショットを読ませるのをやめて、操作で増えるコンテキストを43%削減した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月18日 02:56
- **URL**: [https://zenn.dev/eai/articles/dont-let-agents-see-the-ios-sim-screen](https://zenn.dev/eai/articles/dont-let-agents-see-the-ios-sim-screen)

## 概要

Claude CodeのデスクトップアプリにはiOSシミュレーターを操作するツールがある。個人で作っているiOS向けのMastodonクライアントでは、このツールで実装のたびに画面を確かめさせていた。
しかし、Claudeのコンテキストの大半がスクリーンショットで埋まっているような気がしていた。
そこで、過去のセッションのログ99件を集計して非効率な操作を洗い出し、画面を画像ではなく文字で読む道具を足した。
同じ4つの作業を旧来のやり方と新しいやり方で3回ずつClaudeにやらせて比べた結果は次のとおりである（どれも中央値の和）。



4つの作業の合計
旧来のやり方
新しいやり方
差
...

---

*この記事は自動収集システムによって保存されました。*
