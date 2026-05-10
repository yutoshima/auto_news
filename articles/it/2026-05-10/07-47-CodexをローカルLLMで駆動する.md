---
title: "CodexをローカルLLMで駆動する"
source: "Zenn"
category: "it"
published: 2026-05-10T07:47:08
url: https://zenn.dev/robustonian/articles/codex_with_local_llm
---

# CodexをローカルLLMで駆動する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月10日 07:47
- **URL**: [https://zenn.dev/robustonian/articles/codex_with_local_llm](https://zenn.dev/robustonian/articles/codex_with_local_llm)

## 概要

はじめに
本記事では、ローカルLLMを用いてCodex CLIを駆動するための方法についてまとめる。
!
検証環境はUbuntu 24.04 LTSで行っているが、一般的なLinuxや、Mac、WSL環境でもそのまま使えるかも。


 背景
私は生成AIのベンチマーク評価をすることが趣味の一つなのだが、最近はLLMとClaude CodeやCodexなどのハーネスを組み合わせた際のエージェント性能を評価することが多い。
一般的なハーネスはOpenAI Compatible、すなわちChat Completion APIで動くものが殆どで、それ以外としてClaude CodeはAnth...

---

*この記事は自動収集システムによって保存されました。*
