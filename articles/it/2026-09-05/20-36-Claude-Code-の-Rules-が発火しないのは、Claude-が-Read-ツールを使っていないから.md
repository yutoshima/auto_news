---
title: "Claude Code の Rules が発火しないのは、Claude が Read ツールを使っていないから"
source: "Zenn"
category: "it"
published: 2026-09-05T20:36:54
url: https://zenn.dev/odacchi/articles/claude-code-rules-read-tool
---

# Claude Code の Rules が発火しないのは、Claude が Read ツールを使っていないから

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月05日 20:36
- **URL**: [https://zenn.dev/odacchi/articles/claude-code-rules-read-tool](https://zenn.dev/odacchi/articles/claude-code-rules-read-tool)

## 概要

kawasin73 さんの Claude Code の Rules はもう死んでいる を読みました。
自分も「あるときから挙動がおかしい」と感じてハーネスを見直し、同じ問題までは特定していました。ただ対処が違っていて、記事の解決策（フィーチャーフラグの無効化）を読んで初めて根本原因のほうに手が届いた、という順番です。
原因の発見とフラグの特定はすべて元記事の功績です。この記事は、そこに自分の手元で確認できたことを足して、2 つの直し方の違いを整理するものです。
先に結論から書きます。


paths 付き Rules は Read ツールの実行に相乗りして発火している。Bash の ca...

---

*この記事は自動収集システムによって保存されました。*
