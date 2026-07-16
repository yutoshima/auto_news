---
title: "Claude Code の Plan モードをループエンジニアリングで楽にする"
source: "Zenn"
category: "it"
published: 2026-07-16T07:40:05
url: https://zenn.dev/k_yoshiya/articles/claude-code-plan-mode-loop
---

# Claude Code の Plan モードをループエンジニアリングで楽にする

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月16日 07:40
- **URL**: [https://zenn.dev/k_yoshiya/articles/claude-code-plan-mode-loop](https://zenn.dev/k_yoshiya/articles/claude-code-plan-mode-loop)

## 概要

はじめに
Claude Code の Plan モードを、人間の労力を少なくして使いこなすためのループエンジニアリングをしてみました。この記事を読むと、hook を使って Plan モードに「質問による要件詰め」「実装のサブエージェント委譲」「計画の HTML 確認」を自動で組み込む方法がわかります。

 ねらい
Plan モードの運用に、次の 3 つを組み込みます。うち 1 と 3 の一部（reject 時の再生成サイクル）が反復＝ループ、2 はモデル/セッションの割り当て設計（いわゆるハーネス寄り）です。

Plan モードの初回プロンプト以降のタイピング負荷を AskUserQ...

---

*この記事は自動収集システムによって保存されました。*
