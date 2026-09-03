---
title: "LangGraphのDeltaChannel、400ターンでチェックポイントが77倍の差"
source: "Qiita (Python)"
category: "it"
published: 2026-09-03T00:08:59
url: https://qiita.com/kai_kou/items/2520927f5dbc1a31e231
---

# LangGraphのDeltaChannel、400ターンでチェックポイントが77倍の差

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月03日 00:08
- **URL**: [https://qiita.com/kai_kou/items/2520927f5dbc1a31e231](https://qiita.com/kai_kou/items/2520927f5dbc1a31e231)

## 概要

はじめに
LangGraph でチェックポイントを有効にしたまま長いスレッドを回すと、保存されるデータ量がターン数の二乗で増えていきます。会話履歴を state に貯めるエージェントなら、100 ターン目のチェックポイントは 100 ターン分の履歴を丸ごと書き直しているか...

---

*この記事は自動収集システムによって保存されました。*
