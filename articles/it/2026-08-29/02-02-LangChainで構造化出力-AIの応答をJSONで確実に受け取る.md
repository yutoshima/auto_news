---
title: "LangChainで構造化出力 -- AIの応答をJSONで確実に受け取る"
source: "Qiita (Python)"
category: "it"
published: 2026-08-29T02:02:58
url: https://qiita.com/yukihayama/items/636c83a4412e198c0f45
---

# LangChainで構造化出力 -- AIの応答をJSONで確実に受け取る

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月29日 02:02
- **URL**: [https://qiita.com/yukihayama/items/636c83a4412e198c0f45](https://qiita.com/yukihayama/items/636c83a4412e198c0f45)

## 概要

はじめに
LLMに「JSON形式で出力して」とお願いした経験はないでしょうか。しかし、実際にやってみると次のような問題に直面します。

キー名が「category」になったり「カテゴリ」になったりする（形式のゆれ）
数値を期待したのに文字列で返される（型のゆれ）
必須フィ...

---

*この記事は自動収集システムによって保存されました。*
