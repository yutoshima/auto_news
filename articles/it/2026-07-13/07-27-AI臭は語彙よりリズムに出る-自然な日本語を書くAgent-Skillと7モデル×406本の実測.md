---
title: "AI臭は語彙よりリズムに出る - 自然な日本語を書くAgent Skillと7モデル×406本の実測"
source: "Zenn"
category: "it"
published: 2026-07-13T07:27:42
url: https://zenn.dev/coji/articles/natural-japanese-ai-smell-lint
---

# AI臭は語彙よりリズムに出る - 自然な日本語を書くAgent Skillと7モデル×406本の実測

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月13日 07:27
- **URL**: [https://zenn.dev/coji/articles/natural-japanese-ai-smell-lint](https://zenn.dev/coji/articles/natural-japanese-ai-smell-lint)

## 概要

これはなに？
AIが書いた日本語を自然な日本語に直すAgent Skill、natural-japanese を作りました。Claude CodeやCodexで動きます。プロンプトで「自然に書いて」とお願いする代わりに、AI臭を機械的に検出するlintをスキルの工程に組み込みました。そのlintの閾値は、人間の文章137本とAIの文章406本のコーパスで校正しています。
この記事では、まず「本当に自然になるのか」をbefore/afterで見てもらい、そのあとで先週出たばかりのgpt-5.6を含む7モデルを同じ物差しで診断した結果を紹介します。実装の話はおまけ程度です。

 説明より...

---

*この記事は自動収集システムによって保存されました。*
