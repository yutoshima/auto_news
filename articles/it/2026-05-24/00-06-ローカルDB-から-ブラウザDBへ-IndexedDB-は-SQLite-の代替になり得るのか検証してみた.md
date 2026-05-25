---
title: "ローカルDB から ブラウザDBへ : IndexedDB は SQLite の代替になり得るのか検証してみた"
source: "Zenn"
category: "it"
published: 2026-05-24T00:06:34
url: https://zenn.dev/shinkai_m/articles/4ddf25caef48fb
---

# ローカルDB から ブラウザDBへ : IndexedDB は SQLite の代替になり得るのか検証してみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月24日 00:06
- **URL**: [https://zenn.dev/shinkai_m/articles/4ddf25caef48fb](https://zenn.dev/shinkai_m/articles/4ddf25caef48fb)

## 概要

今回のテーマは 「IndexedDB は SQLite の代替になり得るのか」 です。
最近、ローカルDBを使用しているクライアントアプリのWeb化の話が出ていて、IndexedDBについて考える機会がありました。
そのとき真っ先に気になったのが「IndexedDBって実際どこまで使えるのか」という点でした。
今までブラウザ専用のDBくらいの理解しかしていなかったので、今回ちゃんと触ってみることにしました。
ただし、今回はIndexedDB側の検証にフォーカスします。
SQLiteはあくまで比較対象の文脈として登場するだけで、実際にSQLiteを動かすコードは含みません。
Indexed...

---

*この記事は自動収集システムによって保存されました。*
