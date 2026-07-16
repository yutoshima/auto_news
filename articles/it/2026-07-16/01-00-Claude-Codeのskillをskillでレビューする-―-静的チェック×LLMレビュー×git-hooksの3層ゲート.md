---
title: "Claude Codeのskillをskillでレビューする ― 静的チェック×LLMレビュー×git hooksの3層ゲート"
source: "Zenn"
category: "it"
published: 2026-07-16T01:00:09
url: https://zenn.dev/aldagram_tech/articles/c407ae672c9c0e
---

# Claude Codeのskillをskillでレビューする ― 静的チェック×LLMレビュー×git hooksの3層ゲート

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月16日 01:00
- **URL**: [https://zenn.dev/aldagram_tech/articles/c407ae672c9c0e](https://zenn.dev/aldagram_tech/articles/c407ae672c9c0e)

## 概要

こんにちは！アルダグラムでQAエンジニアをしている千葉です。
私たちのQAチームでは、テスト分析からテスト設計までのQAプロセスをClaude Codeのskill（スキル）として整備し、チームで共同運用しています。
その中心が、これらのQAプロセスを丸ごと任せられるAIエージェント「qa-orchestrator」です。
仕組みと効果は、弊社QAメンバーが記事にしていますのでそちらもご参考ください。
https://zenn.dev/aldagram_tech/articles/4aea4b13671ae3
今ではqa-orchestratorの存在を前提に、固定制インプロセスQAから...

---

*この記事は自動収集システムによって保存されました。*
