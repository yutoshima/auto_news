---
title: "kintoneのgetFieldElementはレコード追加・編集画面ではnullを返す — 仕様の整理と設計の回避策"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-24T06:53:20
url: https://qiita.com/plumeru/items/159296cd69293e4dc5fa
---

# kintoneのgetFieldElementはレコード追加・編集画面ではnullを返す — 仕様の整理と設計の回避策

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月24日 06:53
- **URL**: [https://qiita.com/plumeru/items/159296cd69293e4dc5fa](https://qiita.com/plumeru/items/159296cd69293e4dc5fa)

## 概要

kintoneプラグインで「入力画面のフィールドの横に注記を出す」「候補を絞り込んだセレクトに差し替える」といったUIカスタマイズを作ろうとして、kintone.app.record.getFieldElement() が null しか返さないことに悩んだ経験はないでしょ...

---

*この記事は自動収集システムによって保存されました。*
