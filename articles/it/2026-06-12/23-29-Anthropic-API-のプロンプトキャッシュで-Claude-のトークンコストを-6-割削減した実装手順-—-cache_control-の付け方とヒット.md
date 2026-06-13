---
title: "Anthropic API のプロンプトキャッシュで Claude のトークンコストを 6 割削減した実装手順 — cache_control の付け方とヒット率の確認【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-06-12T23:29:46
url: https://qiita.com/yureki_lab/items/faf7af4dbd77b7253e22
---

# Anthropic API のプロンプトキャッシュで Claude のトークンコストを 6 割削減した実装手順 — cache_control の付け方とヒット率の確認【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年06月12日 23:29
- **URL**: [https://qiita.com/yureki_lab/items/faf7af4dbd77b7253e22](https://qiita.com/yureki_lab/items/faf7af4dbd77b7253e22)

## 概要

はじめに / 対象と前提
Claude API を本番運用していて、ある日 Anthropic のダッシュボードを見たら今月のトークン課金がそこそこ嵩んでいた。原因は明確で、毎リクエスト同じ大きさのシステムプロンプト+ツール定義を投げ直していたから。Anthropic A...

---

*この記事は自動収集システムによって保存されました。*
