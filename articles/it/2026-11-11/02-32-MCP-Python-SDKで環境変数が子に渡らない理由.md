---
title: "MCP Python SDKで環境変数が子に渡らない理由"
source: "Qiita (Python)"
category: "it"
published: 2026-11-11T02:32:16
url: https://qiita.com/hironakamura_ai/items/84557e2723f059bece8a
---

# MCP Python SDKで環境変数が子に渡らない理由

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月11日 02:32
- **URL**: [https://qiita.com/hironakamura_ai/items/84557e2723f059bece8a](https://qiita.com/hironakamura_ai/items/84557e2723f059bece8a)

## 概要

MCP Python SDKのstdio接続を手元で試していて、親に置いたダミーのトークンが子では消えた。同じPythonを普通のsubprocessで起動すると見えている。
MCPサーバーへ渡す環境変数は、名前を決めて明示する。自分はこの方針で組みたい。親の環境を丸ごと渡...

---

*この記事は自動収集システムによって保存されました。*
