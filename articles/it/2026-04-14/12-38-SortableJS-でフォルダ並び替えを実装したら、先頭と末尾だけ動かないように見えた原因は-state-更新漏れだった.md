---
title: "SortableJS でフォルダ並び替えを実装したら、先頭と末尾だけ動かないように見えた原因は state 更新漏れだった"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-04-14T12:38:27
url: https://qiita.com/4Ji/items/7beb91d19c5c691e3645
---

# SortableJS でフォルダ並び替えを実装したら、先頭と末尾だけ動かないように見えた原因は state 更新漏れだった

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年04月14日 12:38
- **URL**: [https://qiita.com/4Ji/items/7beb91d19c5c691e3645](https://qiita.com/4Ji/items/7beb91d19c5c691e3645)

## 概要

SortableJS 利用時に起きる「端だけ戻る」不具合を避ける
SortableJS で並び替えを実装したとき、ログ上は順序変更が進んでいるように見えても、画面更新後に先頭・末尾だけ元に戻ることがあります。原因は多くの場合、ライブラリそのものではなく、保存・復元フローの...

---

*この記事は自動収集システムによって保存されました。*
