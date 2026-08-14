---
title: "MCP サーバーから Claude を逆に呼び出す Sampling 機能の実装 ― createMessage コールバックと権限承認の3つのハマりどころ【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-08-14T23:01:38
url: https://qiita.com/yureki_lab/items/4215e50f647b8a2b8758
---

# MCP サーバーから Claude を逆に呼び出す Sampling 機能の実装 ― createMessage コールバックと権限承認の3つのハマりどころ【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月14日 23:01
- **URL**: [https://qiita.com/yureki_lab/items/4215e50f647b8a2b8758](https://qiita.com/yureki_lab/items/4215e50f647b8a2b8758)

## 概要

はじめに / 対象と前提
MCP(Model Context Protocol)には、サーバー側からクライアント(ホストアプリ)に対して「LLM に代わりに推論させてほしい」とリクエストできる Sampling という仕組みがある。普段 MCP サーバーを作るときは「ツー...

---

*この記事は自動収集システムによって保存されました。*
