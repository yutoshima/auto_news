---
title: "MCP サーバーに Prompts を実装して Claude Code のスラッシュコマンドとして配る手順 — 一覧に出ない・引数が分割される等3つのハマりどころ【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-08-21T23:02:36
url: https://qiita.com/yureki_lab/items/b61bd8f7d979db05101e
---

# MCP サーバーに Prompts を実装して Claude Code のスラッシュコマンドとして配る手順 — 一覧に出ない・引数が分割される等3つのハマりどころ【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月21日 23:02
- **URL**: [https://qiita.com/yureki_lab/items/b61bd8f7d979db05101e](https://qiita.com/yureki_lab/items/b61bd8f7d979db05101e)

## 概要

はじめに / 対象と前提
MCP サーバーの機能というと Tools ばかり話題になるが、仕様には Prompts もある。サーバー側が「定型プロンプト」を配り、クライアントがそれを呼び出す仕組みだ。Claude Code から見ると、これは /mcp__&lt;サーバー名&gt;_...

---

*この記事は自動収集システムによって保存されました。*
