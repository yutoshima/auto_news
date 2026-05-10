---
title: "ブラウザの手書きノートで Apple Pencil の筆圧を取る — `MouseEvent` から `PointerEvent` に乗り換える話と、`getCoalescedEvents()` で 240 Hz サンプリングを取りこぼさない話"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-05-10T00:54:37
url: https://qiita.com/sen-ltd/items/e6b66339e6da21c7986c
---

# ブラウザの手書きノートで Apple Pencil の筆圧を取る — `MouseEvent` から `PointerEvent` に乗り換える話と、`getCoalescedEvents()` で 240 Hz サンプリングを取りこぼさない話

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年05月10日 00:54
- **URL**: [https://qiita.com/sen-ltd/items/e6b66339e6da21c7986c](https://qiita.com/sen-ltd/items/e6b66339e6da21c7986c)

## 概要

Web に手書きノート機能を載せるとき、addEventListener("mousedown", ...) で書き始めると Apple Pencil の筆圧が全部捨てられる、touchstart だけで書き始めると マウスでテストできない、PointerEvent を使...

---

*この記事は自動収集システムによって保存されました。*
