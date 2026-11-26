---
title: "AIエージェントのMemory設計 ― 会話履歴・業務データ・長期Memoryの使い分け"
source: "Zenn"
category: "it"
published: 2026-11-25T05:23:27
url: https://zenn.dev/taru_neko/articles/ai-agent-memory-architecture-2026
---

# AIエージェントのMemory設計 ― 会話履歴・業務データ・長期Memoryの使い分け

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 05:23
- **URL**: [https://zenn.dev/taru_neko/articles/ai-agent-memory-architecture-2026](https://zenn.dev/taru_neko/articles/ai-agent-memory-architecture-2026)

## 概要

AIエージェントでは、過去の会話を記憶し、次の会話に活用するMemoryという仕組みが使われる。
一方、従来のWebアプリケーションでも、セッション管理や業務DBによって情報を保持してきた。AIエージェントだからといって、専用のMemory機構が必要とは限らない。
本記事では、社内の経費精算システムを例に、短期・長期Memoryの構成と既存の仕組みとの使い分けを整理する。さらに、何を記憶するか、情報の更新・削除やセキュリティをどう設計するかを考え、専用の長期Memory機構を採用する条件を明らかにする。

 1. 短期Memoryと長期Memoryの違い
例えば、利用者が次のように依頼す...

---

*この記事は自動収集システムによって保存されました。*
