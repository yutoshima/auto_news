---
title: "【Supabase Auth】別タブから戻ると React の画面がリセットされる原因と対処：SIGNED_IN はログインのときだけじゃない"
source: "Qiita (React)"
category: "it"
published: 2026-11-12T16:16:14
url: https://qiita.com/taikihamamoto/items/65d1c8da59c59310f60a
---

# 【Supabase Auth】別タブから戻ると React の画面がリセットされる原因と対処：SIGNED_IN はログインのときだけじゃない

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年11月12日 16:16
- **URL**: [https://qiita.com/taikihamamoto/items/65d1c8da59c59310f60a](https://qiita.com/taikihamamoto/items/65d1c8da59c59310f60a)

## 概要

結論
Supabase Auth を使った React アプリで、別のタブを開いて戻ってくると、開いていた画面が初期状態に戻りました。エラーは何も出ません。
原因は、onAuthStateChange の SIGNED_IN が タブに戻っただけでも届く ことでした。アプ...

---

*この記事は自動収集システムによって保存されました。*
