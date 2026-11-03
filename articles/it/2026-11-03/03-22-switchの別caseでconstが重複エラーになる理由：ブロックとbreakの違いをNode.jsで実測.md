---
title: "switchの別caseでconstが重複エラーになる理由：ブロックとbreakの違いをNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-03T03:22:00
url: https://qiita.com/ennagara128/items/6ddf56698b1ec6aae3c1
---

# switchの別caseでconstが重複エラーになる理由：ブロックとbreakの違いをNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 03:22
- **URL**: [https://qiita.com/ennagara128/items/6ddf56698b1ec6aae3c1](https://qiita.com/ennagara128/items/6ddf56698b1ec6aae3c1)

## 概要

switchの各caseに同じ名前のconstを書いたら、別の分岐なのにSyntaxErrorになりました。caseラベル自体はスコープを分けません。各caseを波括弧で囲むと名前を分けられますが、breakによる処理の終了は別に必要です。
macOS 27.0.1・Nod...

---

*この記事は自動収集システムによって保存されました。*
