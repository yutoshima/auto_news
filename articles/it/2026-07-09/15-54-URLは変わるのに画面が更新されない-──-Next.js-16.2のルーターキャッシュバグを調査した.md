---
title: "URLは変わるのに画面が更新されない ── Next.js 16.2のルーターキャッシュバグを調査した"
source: "Qiita (React)"
category: "it"
published: 2026-07-09T15:54:36
url: https://qiita.com/tamakiiii/items/17f17d7e3cee63d1c169
---

# URLは変わるのに画面が更新されない ── Next.js 16.2のルーターキャッシュバグを調査した

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年07月09日 15:54
- **URL**: [https://qiita.com/tamakiiii/items/17f17d7e3cee63d1c169](https://qiita.com/tamakiiii/items/17f17d7e3cee63d1c169)

## 概要

TL;DR

Next.js を 15 から 16.2 に上げたら、チェックボックスの複数選択フィルタでルート遷移がおかしくなった

?tag=a&amp;tag=b のように同じキーを複数回並べるクエリで、末尾でない値を外すと、URLは変わるのに一覧が更新されない
原因はクライア...

---

*この記事は自動収集システムによって保存されました。*
