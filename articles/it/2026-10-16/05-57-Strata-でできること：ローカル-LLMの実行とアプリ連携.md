---
title: "Strata でできること：ローカル LLMの実行とアプリ連携"
source: "Zenn"
category: "it"
published: 2026-10-16T05:57:00
url: https://zenn.dev/jtcc/articles/strata-local-llm-app-integration
---

# Strata でできること：ローカル LLMの実行とアプリ連携

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月16日 05:57
- **URL**: [https://zenn.dev/jtcc/articles/strata-local-llm-app-integration](https://zenn.dev/jtcc/articles/strata-local-llm-app-integration)

## 概要

こんにちは。株式会社日本トレカセンターの田島です。
ローカル LLM を使うとき、最初の目標は「手元の PC で回答を生成できること」です。しかし、開発で利用するなら、その先も気になります。
仕様書から条件を抽出できるか。既存のアプリから呼び出せるか。長い資料を渡したとき、どれくらい待つのか。
本記事では、Strata を使ったローカル LLM の実行と、API を通じたアプリ連携を紹介します。さらに、連携先のアプリで使えるかを判断するために、応答時間と出力の正しさをどう確認するかまで整理します。
ストリーミング API の計測結果を掲載しています。本文の非ストリーミング接続例は、測定に...

---

*この記事は自動収集システムによって保存されました。*
