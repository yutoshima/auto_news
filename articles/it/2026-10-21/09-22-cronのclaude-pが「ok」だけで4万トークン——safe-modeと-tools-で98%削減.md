---
title: "cronのclaude -pが「ok」だけで4万トークン——safe-modeと--tools \"\"で98%削減"
source: "Zenn"
category: "it"
published: 2026-10-21T09:22:14
url: https://zenn.dev/yosiki/articles/claude-p-cron-token-diet
---

# cronのclaude -pが「ok」だけで4万トークン——safe-modeと--tools ""で98%削減

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月21日 09:22
- **URL**: [https://zenn.dev/yosiki/articles/claude-p-cron-token-diet](https://zenn.dev/yosiki/articles/claude-p-cron-token-diet)

## 概要

LaunchAgent（macOSのcronのようなもの）から定期的に claude -p "ok" を呼ぶ小さなジョブを動かしています。返事の文面には用がなく、呼び出しが成功するか（認証が切れていないか）だけを見る処理です。
ところが、その返事が毎回こう始まっていました。
Obsidian: mistakes.md / Preferences/ / Agent-Handoff.md を自動読み込みしました。
これは、私が普段の対話用に設定している SessionStart フックの決まり文句です。つまり 「ok」と返させるためだけに、個人用の CLAUDE.md、フックが注入するメモ、...

---

*この記事は自動収集システムによって保存されました。*
