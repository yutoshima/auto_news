---
title: "Notion APIのレート制限で詰まった話 — 3リクエスト/秒を守る実装と、失敗した設計"
source: "Qiita (Python)"
category: "it"
published: 2026-09-19T00:10:21
url: https://qiita.com/yukihayama/items/b6fc82730f80bfdcac18
---

# Notion APIのレート制限で詰まった話 — 3リクエスト/秒を守る実装と、失敗した設計

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月19日 00:10
- **URL**: [https://qiita.com/yukihayama/items/b6fc82730f80bfdcac18](https://qiita.com/yukihayama/items/b6fc82730f80bfdcac18)

## 概要

はじめに
Notion APIでデータベースを一括更新するスクリプトを書いたら、途中から429（rate limited）で止まり、半分だけ更新された状態になりました。しかも厄介なことに、エラーが出るのは決まって処理の後半です。前半は成功しているので「動いている」ように見...

---

*この記事は自動収集システムによって保存されました。*
