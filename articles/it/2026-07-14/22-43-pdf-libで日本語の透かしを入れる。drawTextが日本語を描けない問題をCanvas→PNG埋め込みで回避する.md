---
title: "pdf-libで日本語の透かしを入れる。drawTextが日本語を描けない問題をCanvas→PNG埋め込みで回避する"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-14T22:43:04
url: https://qiita.com/sakutto-panda/items/ada6834b66b32fc7b870
---

# pdf-libで日本語の透かしを入れる。drawTextが日本語を描けない問題をCanvas→PNG埋め込みで回避する

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月14日 22:43
- **URL**: [https://qiita.com/sakutto-panda/items/ada6834b66b32fc7b870](https://qiita.com/sakutto-panda/items/ada6834b66b32fc7b870)

## 概要

3行まとめ

PDFに「社外秘」などの日本語テキスト透かしを入れるツールをブラウザ完結で作った
pdf-lib の drawText は 標準フォントだと日本語を描けない（WinAnsi 限定でエラーになる）。日本語フォントの埋め込みは数MB重い
回避策は Canvas ...

---

*この記事は自動収集システムによって保存されました。*
