---
title: "Claude Code / Codexで「私のlimit、減りすぎ…？」と思ったときに見る記事"
source: "Zenn"
category: "it"
published: 2026-09-29T03:00:09
url: https://zenn.dev/tokium_dev/articles/ai-agent-usage-limit-long-sessions
---

# Claude Code / Codexで「私のlimit、減りすぎ…？」と思ったときに見る記事

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月29日 03:00
- **URL**: [https://zenn.dev/tokium_dev/articles/ai-agent-usage-limit-long-sessions](https://zenn.dev/tokium_dev/articles/ai-agent-usage-limit-long-sessions)

## 概要

こんにちは、TOKIUMの花房です。
Claude CodeやCodexをサブスクリプションで使っていて、以下のように感じることはないでしょうか。

週の半ばで週間上限が尽きる。作業量は先週と変わらないはずなのに
Slack botやcron/launchdからエージェントを動かしていて、体感よりもリミット消費が多い
プロンプトキャッシュにヒットしているはずなのに、やはり減りが多い気がする

Codexの週間上限が急速に減った原因として、私は/goalで一晩動かして自動compact（コンテキストが上限に近づいたとき、エージェントが会話履歴を要約して縮める処理）が何十回も実行されたセッシ...

---

*この記事は自動収集システムによって保存されました。*
