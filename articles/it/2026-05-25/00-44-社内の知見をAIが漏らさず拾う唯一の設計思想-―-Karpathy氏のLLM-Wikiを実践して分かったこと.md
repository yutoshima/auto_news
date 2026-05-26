---
title: "社内の知見をAIが漏らさず拾う唯一の設計思想 ― Karpathy氏のLLM Wikiを実践して分かったこと"
source: "Zenn"
category: "it"
published: 2026-05-25T00:44:18
url: https://zenn.dev/nori_handa/articles/llm-knowledge-base-karpathy-wiki
---

# 社内の知見をAIが漏らさず拾う唯一の設計思想 ― Karpathy氏のLLM Wikiを実践して分かったこと

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月25日 00:44
- **URL**: [https://zenn.dev/nori_handa/articles/llm-knowledge-base-karpathy-wiki](https://zenn.dev/nori_handa/articles/llm-knowledge-base-karpathy-wiki)

## 概要

健適文化という会社をやっています。社内ドキュメントが散らかって検索できない、AIに聞いてもまともな答えが返ってこない、そういう課題に対して、会社のナレッジベースをゼロから構築するお手伝いをしています。この記事はその過程で得た知見をまとめたものです。

 先に結論
社内ドキュメントをベクトルDBに突っ込んでRAGを組んだのに精度が出ない、という問題の原因は「入れ方」にあります。生のドキュメントをそのまま渡すのではなく、LLMが消化できる粒度まで段階的に加工してから渡す。Anthropicがコンテキストエンジニアリングの文脈でprogressive disclosureと呼んでいる設計思想で...

---

*この記事は自動収集システムによって保存されました。*
