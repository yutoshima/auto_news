---
title: "自作 MCP サーバーが Claude Code で認識されない・動かない時のデバッグ手順 — MCP Inspector と stdout 汚染、3つのハマりどころ【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-08-09T23:02:25
url: https://qiita.com/yureki_lab/items/e838ba711f4a75be1ed3
---

# 自作 MCP サーバーが Claude Code で認識されない・動かない時のデバッグ手順 — MCP Inspector と stdout 汚染、3つのハマりどころ【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月09日 23:02
- **URL**: [https://qiita.com/yureki_lab/items/e838ba711f4a75be1ed3](https://qiita.com/yureki_lab/items/e838ba711f4a75be1ed3)

## 概要

はじめに / 対象と前提
自作の MCP サーバーを claude mcp add で登録したのに、Claude Code 側でツールが一切出てこない。エラーも出ない。そんな状況で自分が実際にやっているデバッグ手順をまとめる。
想定読者:

Python か TypeSc...

---

*この記事は自動収集システムによって保存されました。*
