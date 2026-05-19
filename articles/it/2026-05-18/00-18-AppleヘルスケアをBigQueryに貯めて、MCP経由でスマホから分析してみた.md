---
title: "AppleヘルスケアをBigQueryに貯めて、MCP経由でスマホから分析してみた"
source: "Zenn"
category: "it"
published: 2026-05-18T00:18:00
url: https://zenn.dev/jackojacko05/articles/58e0d632be419a
---

# AppleヘルスケアをBigQueryに貯めて、MCP経由でスマホから分析してみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月18日 00:18
- **URL**: [https://zenn.dev/jackojacko05/articles/58e0d632be419a](https://zenn.dev/jackojacko05/articles/58e0d632be419a)

## 概要

こんにちは！某メガベンチャーでデータアナリスト……を３年務めてから、データエンジニアに異動したばかりのじゃっこです🔰
Appleヘルスケアの情報をBigQueryに貯めて、MCP経由でモバイルのClaudeやChatGPTから見られるようにした話です。

Claudeのモバイルアプリからだとグラフの確認もできます

 TL;DR

AppleヘルスケアのデータをBigQueryに貯めて、ClaudeやChatGPTから分析できるようにした
目的は、体重・運動・睡眠・HRV(※心拍変動。高ければコンディションが良い、とみなすことが多い)を長期コンテキストとしてAIに渡すこと
Health ...

---

*この記事は自動収集システムによって保存されました。*
