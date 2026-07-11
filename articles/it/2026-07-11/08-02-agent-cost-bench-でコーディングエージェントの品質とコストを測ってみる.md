---
title: "agent-cost-bench でコーディングエージェントの品質とコストを測ってみる"
source: "Zenn"
category: "it"
published: 2026-07-11T08:02:21
url: https://zenn.dev/aws_japan/articles/agent-cost-bench-model-compare
---

# agent-cost-bench でコーディングエージェントの品質とコストを測ってみる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月11日 08:02
- **URL**: [https://zenn.dev/aws_japan/articles/agent-cost-bench-model-compare](https://zenn.dev/aws_japan/articles/agent-cost-bench-model-compare)

## 概要

はじめに
こんにちは ! ソリューションアーキテクトの いなりく です !
AI コーディングエージェントを使っていると、必ずぶつかる疑問があります。「このタスク、もっと安いモデルでも十分だったのでは ?」「モデルを変えたら品質はどのくらい変わる ?」。カタログスペックや口コミでは答えが出ません。自分のタスクで、実際に測ってみるしかないのです。
この「測ってみる」を簡単にしてくれるツールが、aws-samples に公開されている sample-agent-cost-bench です。本記事ではこのツールの仕組みと使い方を、同梱タスクの中身まで含めて詳しく紹介します。
私自身、このツ...

---

*この記事は自動収集システムによって保存されました。*
