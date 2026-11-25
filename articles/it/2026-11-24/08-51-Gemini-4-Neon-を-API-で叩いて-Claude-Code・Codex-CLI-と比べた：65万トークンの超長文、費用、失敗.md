---
title: "Gemini 4 Neon を API で叩いて Claude Code・Codex CLI と比べた：65万トークンの超長文、費用、失敗"
source: "Zenn"
category: "it"
published: 2026-11-24T08:51:41
url: https://zenn.dev/canly/articles/40e773759da8f8
---

# Gemini 4 Neon を API で叩いて Claude Code・Codex CLI と比べた：65万トークンの超長文、費用、失敗

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月24日 08:51
- **URL**: [https://zenn.dev/canly/articles/40e773759da8f8](https://zenn.dev/canly/articles/40e773759da8f8)

## 概要

カンリーCAIOの萩野です。
2026年11月18日に Google が出した Gemini 4 Neon を、同じ8つの課題で Claude Opus 5.5（Claude Code 経由）と GPT-6.2 Sol（Codex CLI 経由）と比べました。一般向けのまとめは note に書いたので、この記事ではどんなリクエストを送り、どう採点し、いくらかかり、どこで失敗したかを、手順を追える粒度で書きます。プロンプトの全文と正解データの作り方は付録に載せました。
結論を先に書きます。

正解が決まる課題（数学・論理、グラフ読み取り、17万トークンの文書検索、8万トークンのグラフ探索、...

---

*この記事は自動収集システムによって保存されました。*
