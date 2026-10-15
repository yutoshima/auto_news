---
title: "Account-level enforcement guardrail で Claude Code on Bedrock のプロンプト攻撃を入力側でブロックできるか検証した"
source: "DevelopersIO"
category: "it"
published: 2026-10-14T15:51:17
url: https://dev.classmethod.jp/articles/claude-code-bedrock-account-level-guardrail-prompt-attack/
---

# Account-level enforcement guardrail で Claude Code on Bedrock のプロンプト攻撃を入力側でブロックできるか検証した

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 15:51
- **URL**: [https://dev.classmethod.jp/articles/claude-code-bedrock-account-level-guardrail-prompt-attack/](https://dev.classmethod.jp/articles/claude-code-bedrock-account-level-guardrail-prompt-attack/)

## 概要

Claude Code on Bedrock で、ガードレールの紐付け方によってプロンプト攻撃フィルターの入力側の結果がどう変わるかを実機で検証しました。settings.json のヘッダー方式では入力側の攻撃が素通りし、Account-level enforcement guardrail で User prompts を Comprehensive にすると入力側でブロックされました。

---

*この記事は自動収集システムによって保存されました。*
