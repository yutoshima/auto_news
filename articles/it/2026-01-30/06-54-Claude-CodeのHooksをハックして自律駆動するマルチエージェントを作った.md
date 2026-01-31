---
title: "Claude CodeのHooksをハックして自律駆動するマルチエージェントを作った"
source: "Zenn"
category: "it"
published: 2026-01-30T06:54:41
url: https://zenn.dev/zaico/articles/d6b882c78fe4b3
---

# Claude CodeのHooksをハックして自律駆動するマルチエージェントを作った

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年01月30日 06:54
- **URL**: [https://zenn.dev/zaico/articles/d6b882c78fe4b3](https://zenn.dev/zaico/articles/d6b882c78fe4b3)

## 概要

はじめに

 作ったもの
Claude Codeを拡張して、複数のAIエージェントが協調してタスクを実行するシステムを作りました。タスクの自動分解、セッション間の状態継続、ルールの自動適用、問題検出時の自己修正を実現しています。

ソースコード: 本記事で解説するシステムのソースコードはGitHubで公開しています。
https://github.com/taro-taryo/chaincrew



 なぜ作ったか
コーディングルールを守らせたり、複数のタスクを順序通りに実行させたりする作業は、人間がやると手間がかかります。
「既存コードの命名規則に合わせる」「このプロジェクトでは...

---

*この記事は自動収集システムによって保存されました。*
