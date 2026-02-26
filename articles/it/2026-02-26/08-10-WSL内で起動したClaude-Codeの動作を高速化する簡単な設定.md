---
title: "WSL内で起動したClaude Codeの動作を高速化する簡単な設定"
source: "Zenn"
category: "it"
published: 2026-02-26T08:10:09
url: https://zenn.dev/momonga/articles/ee5b114e038938
---

# WSL内で起動したClaude Codeの動作を高速化する簡単な設定

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月26日 08:10
- **URL**: [https://zenn.dev/momonga/articles/ee5b114e038938](https://zenn.dev/momonga/articles/ee5b114e038938)

## 概要

TL;DR
.bashrc に以下の設定を追加してください。
# Workaround to prevent Claude Code from repeatedly spawning powershell.exe.
# ref: https://github.com/anthropics/claude-code/issues/14352
export CLAUDE_CODE_SKIP_WINDOWS_PROFILE=1
export USERPROFILE="/mnt/c/Users/&lt;your_windows_username&gt;"
&lt;your_windows_us...

---

*この記事は自動収集システムによって保存されました。*
