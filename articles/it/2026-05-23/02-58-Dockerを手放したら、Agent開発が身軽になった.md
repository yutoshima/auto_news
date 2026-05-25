---
title: "Dockerを手放したら、Agent開発が身軽になった"
source: "Zenn"
category: "it"
published: 2026-05-23T02:58:14
url: https://zenn.dev/mofuteq/articles/93a1920e7a8d62
---

# Dockerを手放したら、Agent開発が身軽になった

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月23日 02:58
- **URL**: [https://zenn.dev/mofuteq/articles/93a1920e7a8d62](https://zenn.dev/mofuteq/articles/93a1920e7a8d62)

## 概要

Agentを作っていました。
最初は、LLMに入力を渡して、structured outputを返すくらいの小さなもののつもりでした。
でも気がつくと、手元では docker compose が育っていました。
Postgres
Redis
Qdrant
Langfuse
ClickHouse
MinIO
Backend
Frontend
Worker
うおw、Agentどこいった。
もちろん、自前で立てると理解は深まります。
各componentの役割も分かるし、データの流れも見える。
ただ、ある段階を超えると、Agentを作っているのか、周辺インフラを飼育しているのか分からなくなる。...

---

*この記事は自動収集システムによって保存されました。*
