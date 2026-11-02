---
title: "LangChainエージェントがRecursion limit 25で止まった — 同じToolを無限に呼ぶ夜間バッチを3つのガードで断つ完全実装"
source: "Qiita (Python)"
category: "it"
published: 2026-11-02T02:03:15
url: https://qiita.com/yukihayama/items/37ab443f33b333e6b05b
---

# LangChainエージェントがRecursion limit 25で止まった — 同じToolを無限に呼ぶ夜間バッチを3つのガードで断つ完全実装

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月02日 02:03
- **URL**: [https://qiita.com/yukihayama/items/37ab443f33b333e6b05b](https://qiita.com/yukihayama/items/37ab443f33b333e6b05b)

## 概要

毎晩2時、LangChainエージェントに外部API照会をさせる夜間バッチを動かしています。ある朝、ログには「Recursion limit of 25 reached」の1行だけ。タスク120件のうち完了は0件でした。エージェントは失敗したTool呼び出しを、引数を少し変...

---

*この記事は自動収集システムによって保存されました。*
