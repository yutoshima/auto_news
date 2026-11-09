---
title: "【X】ブラウザ経由の自動投稿が時々落ちる原因をCDPで切り分けた手順（intentをやめた話）"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-08T22:44:06
url: https://qiita.com/kusarikakemron/items/d4303ebae8260a6859ae
---

# 【X】ブラウザ経由の自動投稿が時々落ちる原因をCDPで切り分けた手順（intentをやめた話）

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月08日 22:44
- **URL**: [https://qiita.com/kusarikakemron/items/d4303ebae8260a6859ae](https://qiita.com/kusarikakemron/items/d4303ebae8260a6859ae)

## 概要

X の返信と予約投稿を、API ではなく専用ブラウザ（CDP）から出す仕組みで、投稿が2日近く時々落ち続けました。結論は「投稿の小窓（intent/post）を通るのをやめ、ホームと返信先ページの入力欄に直接入れる」です。途中で探査が1回通ったのを見て「直った」と書き、1時...

---

*この記事は自動収集システムによって保存されました。*
