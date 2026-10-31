---
title: "Claude Code の PreToolUse フックで git add -A や reset --hard を機械的に止める(誤検知の避け方つき)"
source: "Qiita (Python)"
category: "it"
published: 2026-10-31T00:57:42
url: https://qiita.com/takamatt_ai/items/2ed447a87f8d7900cea0
---

# Claude Code の PreToolUse フックで git add -A や reset --hard を機械的に止める(誤検知の避け方つき)

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月31日 00:57
- **URL**: [https://qiita.com/takamatt_ai/items/2ed447a87f8d7900cea0](https://qiita.com/takamatt_ai/items/2ed447a87f8d7900cea0)

## 概要

何に困ったか
複数の Claude Code セッションを、同じ1つのクローンで同時に動かしています。
CLAUDE.md には「git add -A と reset --hard と stash は使わない」と書いていました。
ただ、文章での「お願い」は、守られないこと...

---

*この記事は自動収集システムによって保存されました。*
