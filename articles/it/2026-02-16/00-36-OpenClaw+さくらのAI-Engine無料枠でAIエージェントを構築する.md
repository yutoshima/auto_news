---
title: "OpenClaw+さくらのAI Engine無料枠でAIエージェントを構築する"
source: "Zenn"
category: "it"
published: 2026-02-16T00:36:04
url: https://zenn.dev/yskst/articles/3309f73a813d1a
---

# OpenClaw+さくらのAI Engine無料枠でAIエージェントを構築する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月16日 00:36
- **URL**: [https://zenn.dev/yskst/articles/3309f73a813d1a](https://zenn.dev/yskst/articles/3309f73a813d1a)

## 概要

はじめに

OpenClawのトークン消費が激しいのでClaude以外のModel選択肢を探してみました。
強いマシンを買ってローカルLLMを立てれば使い放題だけどそこまでコストはかけられないなぁと思っていたところ、さくらのAI Engineの無料枠が3,000リクエスト/月とかなり太っ腹だったので試してみた、という記事です。

 事前準備
まずVPSなどでOpenClawを動かすサーバ環境を用意します。
メモリ4GB以上が推奨のようですが、
自分の環境では2vCPU/2GBメモリのサーバでも(若干もっさりしますが)一応動きました。
!
OpenClawは稼働している環境のファイルア...

---

*この記事は自動収集システムによって保存されました。*
