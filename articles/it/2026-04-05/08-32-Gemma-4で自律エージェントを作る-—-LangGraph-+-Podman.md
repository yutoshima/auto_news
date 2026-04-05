---
title: "Gemma 4で自律エージェントを作る — LangGraph + Podman"
source: "Zenn"
category: "it"
published: 2026-04-05T08:32:43
url: https://zenn.dev/nekoroko/articles/7f22e9c8557aea
---

# Gemma 4で自律エージェントを作る — LangGraph + Podman

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月05日 08:32
- **URL**: [https://zenn.dev/nekoroko/articles/7f22e9c8557aea](https://zenn.dev/nekoroko/articles/7f22e9c8557aea)

## 概要

Claude CoworkもOpenClawも使わず、ローカルLLMで自律エージェントを自作した。
理由は2つあります。1つは、クライアント案件のデータを外部APIに投げられない現場がある。。もう1つは、Gemma 4がApache 2.0で出た今、ローカルで同じことがどこまでできるのか、実務者として知っておきたかった。
この記事では、Gemma 4 + LangGraphを使って「タスクを受け取り、必要ならツールを使い、なければ自分でコードを書いて実行する」自律エージェントをRTX 4060 1枚で構築した全手順を共有します。

 背景：AIエージェント自動実行の現在地
2026年に入...

---

*この記事は自動収集システムによって保存されました。*
