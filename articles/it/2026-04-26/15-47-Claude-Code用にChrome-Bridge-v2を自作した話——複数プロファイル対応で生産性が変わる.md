---
title: "Claude Code用にChrome Bridge v2を自作した話——複数プロファイル対応で生産性が変わる"
source: "Qiita (Python)"
category: "it"
published: 2026-04-26T15:47:08
url: https://qiita.com/mistudio0902/items/0cf60686fc1498b82e07
---

# Claude Code用にChrome Bridge v2を自作した話——複数プロファイル対応で生産性が変わる

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年04月26日 15:47
- **URL**: [https://qiita.com/mistudio0902/items/0cf60686fc1498b82e07](https://qiita.com/mistudio0902/items/0cf60686fc1498b82e07)

## 概要

TL;DR
Claude Codeから複数Chromeプロファイルを同時操作したい開発者向けに、自作Chrome Bridge v2の設計と実装手順をまとめました。3層構造（拡張 → WebSocket → MCPサーバー）でプロファイル分離を実現し、安定した接続と30個...

---

*この記事は自動収集システムによって保存されました。*
