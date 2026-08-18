---
title: "検索機能のないAPIに検索機能を足す：Python標準のsqlite3だけでやる"
source: "Qiita (Python)"
category: "it"
published: 2026-08-18T22:28:00
url: https://qiita.com/choco_monja/items/2e77161ca4503cd183ae
---

# 検索機能のないAPIに検索機能を足す：Python標準のsqlite3だけでやる

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月18日 22:28
- **URL**: [https://qiita.com/choco_monja/items/2e77161ca4503cd183ae](https://qiita.com/choco_monja/items/2e77161ca4503cd183ae)

## 概要

前提：API が検索させてくれないことがある
公開 API を使っていると、こういう仕様にときどき出会います。

日付での絞り込みができない
ソート順が固定
1 回に取れる件数に上限がある
ページ送りは offset だけ

こうなると「先月の分を条件付きで見たい」という...

---

*この記事は自動収集システムによって保存されました。*
