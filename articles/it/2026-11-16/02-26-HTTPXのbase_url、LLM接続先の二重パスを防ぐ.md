---
title: "HTTPXのbase_url、LLM接続先の二重パスを防ぐ"
source: "Qiita (Python)"
category: "it"
published: 2026-11-16T02:26:26
url: https://qiita.com/hironakamura_ai/items/5f7060df01465345ae39
---

# HTTPXのbase_url、LLM接続先の二重パスを防ぐ

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月16日 02:26
- **URL**: [https://qiita.com/hironakamura_ai/items/5f7060df01465345ae39](https://qiita.com/hironakamura_ai/items/5f7060df01465345ae39)

## 概要

「先頭の / はホスト直下から始まる」。2026年11月14日付の開発者ブログ「datasette-llm 0.1a11」で互換エンドポイント対応を知り、HTTPXでも確かめたら、この予想が外れた。
HTTPX 0.28.1の Client(base_url=...) は、...

---

*この記事は自動収集システムによって保存されました。*
