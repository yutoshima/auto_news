---
title: "業務文書RAGのレイアウトカテゴリ設計（5/5）Caption・Footnote・Header/Footer・Formula・Codeをどう扱うか"
source: "Qiita (Python)"
category: "it"
published: 2026-09-09T00:24:47
url: https://qiita.com/engchina/items/c8f53a9c4586088d78ea
---

# 業務文書RAGのレイアウトカテゴリ設計（5/5）Caption・Footnote・Header/Footer・Formula・Codeをどう扱うか

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月09日 00:24
- **URL**: [https://qiita.com/engchina/items/c8f53a9c4586088d78ea](https://qiita.com/engchina/items/c8f53a9c4586088d78ea)

## 概要

先に結論
Picture、Table、Form、List まで作ると、RAG はかなり実用に近づきます。
ただ、最後に残る category を雑に扱うと、検索ノイズや citation のズレが出ます。
残りの category は、全部を同じように chunk にする...

---

*この記事は自動収集システムによって保存されました。*
