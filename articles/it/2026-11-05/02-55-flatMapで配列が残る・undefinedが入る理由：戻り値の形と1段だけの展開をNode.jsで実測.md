---
title: "flatMapで配列が残る・undefinedが入る理由：戻り値の形と1段だけの展開をNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-05T02:55:30
url: https://qiita.com/ennagara128/items/2b69aeae5cddaeaf2879
---

# flatMapで配列が残る・undefinedが入る理由：戻り値の形と1段だけの展開をNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 02:55
- **URL**: [https://qiita.com/ennagara128/items/2b69aeae5cddaeaf2879](https://qiita.com/ennagara128/items/2b69aeae5cddaeaf2879)

## 概要

flatMap()に置き換えたのに配列が残ったり、除外したつもりの位置にundefinedが入ったりする場合、コールバックが返した値の形を調べると切り分けられます。今回は「何でも再帰的に平らにする」とは考えず、返した配列を1段だけ展開する動きを、小さなデータで確かめます。
...

---

*この記事は自動収集システムによって保存されました。*
