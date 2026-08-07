---
title: "`await` を書いたのに、次の処理が先に走った — forEach は async 関数を待たない"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-06T15:30:05
url: https://qiita.com/daisuke-nagata/items/95cce82f3e7b8c8847ac
---

# `await` を書いたのに、次の処理が先に走った — forEach は async 関数を待たない

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月06日 15:30
- **URL**: [https://qiita.com/daisuke-nagata/items/95cce82f3e7b8c8847ac](https://qiita.com/daisuke-nagata/items/95cce82f3e7b8c8847ac)

## 概要

await を書いたのに、forEach を抜けた直後に次の処理が走った。原因はバグではなく仕様。Array.prototype.forEach はコールバックの戻り値を捨てるので、async 関数が返した Promise は誰にも待たれない。直すのは、順番が要るなら fo...

---

*この記事は自動収集システムによって保存されました。*
