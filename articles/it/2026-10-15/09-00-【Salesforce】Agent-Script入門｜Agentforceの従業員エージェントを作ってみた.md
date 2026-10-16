---
title: "【Salesforce】Agent Script入門｜Agentforceの従業員エージェントを作ってみた"
source: "Zenn"
category: "it"
published: 2026-10-15T09:00:14
url: https://zenn.dev/actbe_tech/articles/57561ffebaf9ed
---

# 【Salesforce】Agent Script入門｜Agentforceの従業員エージェントを作ってみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 09:00
- **URL**: [https://zenn.dev/actbe_tech/articles/57561ffebaf9ed](https://zenn.dev/actbe_tech/articles/57561ffebaf9ed)

## 概要

はじめに
Agentforceの指示文に「必ず取引先を確認してから回答してください」と書いたのに、確認が飛ばされて、そのまま回答されてしまった。
Agentforceでエージェントを作っていると、こんな場面に出会うことがあります。
LLMは賢いですが、少し気まぐれなところがあります。
「必ず」と書いても、必ず動くとは限りません。業務で使うとなると、「ここだけは毎回同じ動きをしてほしい」という部分が出てきます。
そこで使えるのが Agent Script です。
気まぐれでもよい部分はLLMに任せ、毎回同じ動きをしてほしい部分はコードで書く。
Agent Scriptはその線引きができ...

---

*この記事は自動収集システムによって保存されました。*
