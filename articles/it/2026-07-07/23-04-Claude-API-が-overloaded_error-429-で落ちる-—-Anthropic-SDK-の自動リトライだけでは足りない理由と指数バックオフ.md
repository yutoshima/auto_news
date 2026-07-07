---
title: "Claude API が overloaded_error / 429 で落ちる — Anthropic SDK の自動リトライだけでは足りない理由と指数バックオフ+ジッターの実装手順【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-07-07T23:04:39
url: https://qiita.com/yureki_lab/items/cbd573de10db20193ab9
---

# Claude API が overloaded_error / 429 で落ちる — Anthropic SDK の自動リトライだけでは足りない理由と指数バックオフ+ジッターの実装手順【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年07月07日 23:04
- **URL**: [https://qiita.com/yureki_lab/items/cbd573de10db20193ab9](https://qiita.com/yureki_lab/items/cbd573de10db20193ab9)

## 概要

はじめに / 対象と前提
Claude API(Anthropic Python SDK)でそこそこの量のリクエストを投げていると、ある日突然こういうのに出くわす。
anthropic.InternalServerError: Error code: 529 - {'ty...

---

*この記事は自動収集システムによって保存されました。*
