---
title: "Claude Codeが書いたコードを読む代わりにやっていること"
source: "Zenn"
category: "it"
published: 2026-11-16T05:04:44
url: https://zenn.dev/linkedge/articles/claude-code-instead-of-reading-code
---

# Claude Codeが書いたコードを読む代わりにやっていること

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月16日 05:04
- **URL**: [https://zenn.dev/linkedge/articles/claude-code-instead-of-reading-code](https://zenn.dev/linkedge/articles/claude-code-instead-of-reading-code)

## 概要

はじめに
個人で作っているWebアプリの実装を、最近はClaude Codeに任せています。PRが増えて全部は読みきれなくなり、ほとんどコードを読まずにマージしています。テストもレビューも動作確認も、AIにやらせています。
ところが、作業を終える前にテストを回すはずの仕組みが、一度もテストを動かしていませんでした。毎回0.1秒かからずに通っていて、確認は全部通っていたので、しばらく気づきませんでした。
この件もあって、コードを読まなくなった代わりに、今は次の2つをしています。

受け入れ条件を決める
確認の記録を読む

コーディングエージェントにテストやレビューまで任せて、PRを読ま...

---

*この記事は自動収集システムによって保存されました。*
