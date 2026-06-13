---
title: "Bedrock AgentCore + Strands Agents SDK で作る、使うほど賢くなる社内 RAG ボット"
source: "Zenn"
category: "it"
published: 2026-06-12T03:38:31
url: https://zenn.dev/pksha/articles/agentcore-strands-self-improving-rag
---

# Bedrock AgentCore + Strands Agents SDK で作る、使うほど賢くなる社内 RAG ボット

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月12日 03:38
- **URL**: [https://zenn.dev/pksha/articles/agentcore-strands-self-improving-rag](https://zenn.dev/pksha/articles/agentcore-strands-self-improving-rag)

## 概要

1. はじめに
PKSHA Technology でソフトウェアエンジニアをしている成川（@eve_n）です。
私のチームでは、社内ヘルプデスク向けの Slack RAG ボットを運用しています。社員から日々寄せられる問い合わせ（社内手続きや各種 SaaS の使い方、備品・申請まわりなど）に、Slack 上で自動応答するボットです。ヘルプデスク担当者の負荷を下げ、社員が自己解決できる割合を増やすことを目的に、自分たちで開発した社内専用ツールです。
先日これを Bedrock AgentCore + Strands Agents SDK をベースに作り直しました。
!
本記事で扱うのは...

---

*この記事は自動収集システムによって保存されました。*
