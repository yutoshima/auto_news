---
title: "Agent Skillは振る舞いとナレッジを分けて設計する"
source: "Zenn"
category: "it"
published: 2026-09-09T10:00:05
url: https://zenn.dev/socialplus/articles/f5d9e28470eb99
---

# Agent Skillは振る舞いとナレッジを分けて設計する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月09日 10:00
- **URL**: [https://zenn.dev/socialplus/articles/f5d9e28470eb99](https://zenn.dev/socialplus/articles/f5d9e28470eb99)

## 概要

どうもこんにちは、たくびーです。
弊社ではClaudeのチームプランに契約しており、開発者全員がClaude Codeを使うことができます。
希望者はChatGPTのチームプランも使えてCodexを併用することも可能です。
私はAI開発環境整備の一環でルールやスキルの作成やメンテナンスをすることが多いです。
そこで最近はエージェントスキルの設計方針について考えることが多く、現時点でどういう観点でスキルを作成しているかということをご紹介したいと思います。
!
記事の内容は人間が書いていますが、調査などにAIを使用しています。


 TL;DR

スキルを書くときは振る舞いとナレッジを分ける...

---

*この記事は自動収集システムによって保存されました。*
