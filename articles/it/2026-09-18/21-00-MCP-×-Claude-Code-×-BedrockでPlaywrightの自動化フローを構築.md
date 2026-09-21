---
title: "MCP × Claude Code × BedrockでPlaywrightの自動化フローを構築"
source: "Zenn"
category: "it"
published: 2026-09-18T21:00:05
url: https://zenn.dev/hirata_infosys/articles/598068e56ae342
---

# MCP × Claude Code × BedrockでPlaywrightの自動化フローを構築

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月18日 21:00
- **URL**: [https://zenn.dev/hirata_infosys/articles/598068e56ae342](https://zenn.dev/hirata_infosys/articles/598068e56ae342)

## 概要

はじめに
既存のシステムに対し、AIエージェントを導入しようとする場合、更新系は制約事項が多々あります。基本的にエージェントなどからデータを直接更新することは、禁止されているシステムが多いのではないでしょうか？
そこで、Playwrightを使用することでインターフェースは既存の画面を使用し、人の判断をLLMで代替する一つのAIエージェントの実現手段として、Playwrightの検証を行ってみました。
今回の検証では、社内のWEBシステム（勤怠管理）をPlaywrightで操作しています。
本記事ではPlaywrightの自動化フローを作成するにあたり、MCP × Claude Co...

---

*この記事は自動収集システムによって保存されました。*
