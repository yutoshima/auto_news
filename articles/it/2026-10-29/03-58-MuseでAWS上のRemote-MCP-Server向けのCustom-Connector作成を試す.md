---
title: "MuseでAWS上のRemote MCP Server向けのCustom Connector作成を試す"
source: "DevelopersIO"
category: "it"
published: 2026-10-29T03:58:16
url: https://dev.classmethod.jp/articles/shuntaka-muse-custom-connector-remote-mcp/
---

# MuseでAWS上のRemote MCP Server向けのCustom Connector作成を試す

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月29日 03:58
- **URL**: [https://dev.classmethod.jp/articles/shuntaka-muse-custom-connector-remote-mcp/](https://dev.classmethod.jp/articles/shuntaka-muse-custom-connector-remote-mcp/)

## 概要

Metaのパーソナルアシスタント「Muse」をAWSの会議室予約アプリと連携させ、DCR対応の認証ありと認証なしの2つのMCP接続方式を検証しました。認証ありはMuseにコネクターとして登録されて完全に統合される一方で、認証なしはコネクター画面に表示されないながらも、Muse内部のクライアントから直接ツール呼び出しが可能な違いが見えてきます。

---

*この記事は自動収集システムによって保存されました。*
