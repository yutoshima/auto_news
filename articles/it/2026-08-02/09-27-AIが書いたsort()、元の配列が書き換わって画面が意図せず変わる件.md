---
title: "AIが書いたsort()、元の配列が書き換わって画面が意図せず変わる件"
source: "Qiita (React)"
category: "it"
published: 2026-08-02T09:27:00
url: https://qiita.com/ennagara128/items/5bcc4e448048a1e15f5d
---

# AIが書いたsort()、元の配列が書き換わって画面が意図せず変わる件

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年08月02日 09:27
- **URL**: [https://qiita.com/ennagara128/items/5bcc4e448048a1e15f5d](https://qiita.com/ennagara128/items/5bcc4e448048a1e15f5d)

## 概要

起きたこと
Reactでリストを日付順に並べ替えて表示する処理をAIに書いてもらったところ、なぜか元のstateの並び順まで変わってしまう不具合が起きました。
const [items, setItems] = useState(originalItems);

func...

---

*この記事は自動収集システムによって保存されました。*
