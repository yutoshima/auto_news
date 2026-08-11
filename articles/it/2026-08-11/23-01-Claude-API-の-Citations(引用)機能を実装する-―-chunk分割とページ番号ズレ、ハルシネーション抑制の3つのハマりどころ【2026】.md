---
title: "Claude API の Citations(引用)機能を実装する ― chunk分割とページ番号ズレ、ハルシネーション抑制の3つのハマりどころ【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-08-11T23:01:52
url: https://qiita.com/yureki_lab/items/42da9534a5c1fd8e4ed5
---

# Claude API の Citations(引用)機能を実装する ― chunk分割とページ番号ズレ、ハルシネーション抑制の3つのハマりどころ【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月11日 23:01
- **URL**: [https://qiita.com/yureki_lab/items/42da9534a5c1fd8e4ed5](https://qiita.com/yureki_lab/items/42da9534a5c1fd8e4ed5)

## 概要

はじめに / 対象と前提
Claude API で RAG(検索拡張生成)っぽいことをやると、必ず突き当たるのが「この回答、本当にソース文書のどこに書いてあるの?」問題です。自分で prompt に「引用元を明記して」と書いても、Claude は律儀に答えてくれる時もあれ...

---

*この記事は自動収集システムによって保存されました。*
