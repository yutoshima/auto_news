---
title: "なぜAnthropicはプロンプトにXMLタグを推奨するのか──Markdownとの構造的な違い"
source: "Zenn"
category: "it"
published: 2026-05-24T04:37:14
url: https://zenn.dev/yun_bow/articles/a339e1d31a4c43
---

# なぜAnthropicはプロンプトにXMLタグを推奨するのか──Markdownとの構造的な違い

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月24日 04:37
- **URL**: [https://zenn.dev/yun_bow/articles/a339e1d31a4c43](https://zenn.dev/yun_bow/articles/a339e1d31a4c43)

## 概要

はじめに
「Markdown で書けばAIが読みやすいはず」——そう思って CLAUDE.md や RAG のソースドキュメントを Markdown で整備してきた人は多いはずだ。
しかし実際にプロンプトエンジニアリングを突き詰めていくと、システムプロンプトの構造化や RAG のチャンク設計という特定の用途に絞った文脈では、構造が複雑なコンテキストほど HTML や XML ライクな構造で渡したほうが AI の解釈精度が上がる という経験則に直面することがある。
本稿では「なぜ Markdown より HTML が特定シナリオで AI に有利になりうるのか」を、言語設計・LLM の学...

---

*この記事は自動収集システムによって保存されました。*
