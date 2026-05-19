---
title: "React CompilerをannotationモードとOxlintで漸進的に導入する"
source: "Zenn"
category: "it"
published: 2026-05-19T10:00:00
url: https://zenn.dev/dress_code/articles/92dfb9206f50f3
---

# React CompilerをannotationモードとOxlintで漸進的に導入する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月19日 10:00
- **URL**: [https://zenn.dev/dress_code/articles/92dfb9206f50f3](https://zenn.dev/dress_code/articles/92dfb9206f50f3)

## 概要

React CompilerをannotationモードとOxlintで漸進的に導入する

 はじめに
こんにちは。ぷーじ（@yug1224）です。
約7,500ファイルのTypeScriptプロジェクトにReact Compilerを導入しました。本記事では、annotationモードとOxlintで、all モードの一括適用ではなく、段階的に Compiler を広げた進め方を紹介します。

 導入の背景
最初は "all" モードをローカルで気軽に試してみたのですが、TanStack Table v8を使ったテーブルが軒並み壊れ、react-hook-formのフォームが無限ルー...

---

*この記事は自動収集システムによって保存されました。*
