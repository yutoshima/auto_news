---
title: "自作MCPサーバーのトークン消費を9割削減するTips ── MCPの退避パターン"
source: "Zenn"
category: "it"
published: 2026-05-01T01:10:07
url: https://zenn.dev/aircloset/articles/4c5f49f89db19f
---

# 自作MCPサーバーのトークン消費を9割削減するTips ── MCPの退避パターン

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月01日 01:10
- **URL**: [https://zenn.dev/aircloset/articles/4c5f49f89db19f](https://zenn.dev/aircloset/articles/4c5f49f89db19f)

## 概要

みなさまこんにちは！エアークローゼットでCTOをしている辻です。
これまで 社内MCP群の全体像、DB Graph MCP、Biz Graph、Sandbox MCP と、社内向けに作っているMCPサーバーを順に紹介してきました。
今回はその運用の中で見えてきた、自作MCPサーバーのトークン消費を減らすTips の話を書きます。

 困りごと：MCPは意外とトークンを食う
MCPでAIエージェントを拡張するとき、最初に遭遇するのが トークン消費が想定より多い という現実です。
MCPのツール呼び出しは、結局のところ JSON-RPC over HTTP です。AIが送る引数も、ツールが返...

---

*この記事は自動収集システムによって保存されました。*
