---
title: "MCPサーバーに日付が「今日」で飛んでくる — AIの引数を4つのガードで弾くFastMCP完全実装"
source: "Qiita (Python)"
category: "it"
published: 2026-11-11T02:06:03
url: https://qiita.com/yukihayama/items/8f49e850846ba2bf52df
---

# MCPサーバーに日付が「今日」で飛んでくる — AIの引数を4つのガードで弾くFastMCP完全実装

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月11日 02:06
- **URL**: [https://qiita.com/yukihayama/items/8f49e850846ba2bf52df](https://qiita.com/yukihayama/items/8f49e850846ba2bf52df)

## 概要

夜間のタスク整理エージェントが、ある朝から検索結果を1件も返さなくなりました。原因特定に3日かかった私の失敗です。ログを見ると、MCPツールに渡っていたのは due_from: "今日"。AIはschemaを読まず、相対日付をそのまま送ってきました。関数の中で日付を解釈する...

---

*この記事は自動収集システムによって保存されました。*
