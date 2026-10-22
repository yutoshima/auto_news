---
title: "Amazon Bedrock Guardrails を AnswerCarefully で試してみた\n\n日本語訳: Amazon Bedrock Guardrails を AnswerCarefully で試してみた"
source: "Zenn"
category: "it"
published: 2026-10-21T05:08:24
url: https://zenn.dev/aws_japan/articles/bedrock-guardrails-japanese-tier
---

# Amazon Bedrock Guardrails を AnswerCarefully で試してみた

日本語訳: Amazon Bedrock Guardrails を AnswerCarefully で試してみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月21日 05:08
- **URL**: [https://zenn.dev/aws_japan/articles/bedrock-guardrails-japanese-tier](https://zenn.dev/aws_japan/articles/bedrock-guardrails-japanese-tier)

## 概要

Amazon Bedrock Guardrails は、生成 AI モデルに届く前の入力と、モデルが生成した後の出力を検査します。有害だと判定した内容は、利用者へ渡さずにブロックできます。
ユーザー入力 → Guardrail の入力判定 → モデル → Guardrail の出力判定 → 利用者
この記事では、Guardrail が入力や出力を遮断することを「ブロック」、Guardrail を通過した質問への回答をモデル自身が断ることを「拒否」と呼びます。
Guardrails には、判定に使う仕組みが異なる Classic と Standard の 2 つの Tier があります。日...

---

*この記事は自動収集システムによって保存されました。*
