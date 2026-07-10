---
title: "Claude API の Files API でPDF・画像を使い回す実装 — base64貼り付けをやめて3つのハマりどころを潰した話【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-07-10T23:01:34
url: https://qiita.com/yureki_lab/items/e4a75872c2dcb4aa26ac
---

# Claude API の Files API でPDF・画像を使い回す実装 — base64貼り付けをやめて3つのハマりどころを潰した話【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年07月10日 23:01
- **URL**: [https://qiita.com/yureki_lab/items/e4a75872c2dcb4aa26ac](https://qiita.com/yureki_lab/items/e4a75872c2dcb4aa26ac)

## 概要

はじめに / 対象と前提
Claude API(Anthropic Python SDK)で PDF や画像を繰り返しリクエストに渡す処理を書いたことがある人向け。毎回 base64 にエンコードして content に埋め込んでいると、リクエストサイズが膨らんで通信も遅...

---

*この記事は自動収集システムによって保存されました。*
