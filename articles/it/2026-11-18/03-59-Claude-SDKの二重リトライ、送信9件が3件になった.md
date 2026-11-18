---
title: "Claude SDKの二重リトライ、送信9件が3件になった"
source: "Qiita (Python)"
category: "it"
published: 2026-11-18T03:59:55
url: https://qiita.com/hironakamura_ai/items/f92209d77e1e46c90d15
---

# Claude SDKの二重リトライ、送信9件が3件になった

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月18日 03:59
- **URL**: [https://qiita.com/hironakamura_ai/items/f92209d77e1e46c90d15](https://qiita.com/hironakamura_ai/items/f92209d77e1e46c90d15)

## 概要

3回のループから、送信が9件出た。ClaudeのPython SDKに429を返すモックを作り、今日、手元で数えた。
自分は再実行のコードを確認してて、外側の回数だけではログが足りないな、と感じた。SDK内の再試行も数えたい。

外側3回、SDKの内側も3回
検証環境はma...

---

*この記事は自動収集システムによって保存されました。*
