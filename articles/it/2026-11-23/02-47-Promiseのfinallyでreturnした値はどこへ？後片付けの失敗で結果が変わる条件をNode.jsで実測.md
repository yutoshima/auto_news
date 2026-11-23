---
title: "Promiseのfinallyでreturnした値はどこへ？後片付けの失敗で結果が変わる条件をNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-23T02:47:13
url: https://qiita.com/ennagara128/items/35ce039e95aeaa50bbd7
---

# Promiseのfinallyでreturnした値はどこへ？後片付けの失敗で結果が変わる条件をNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 02:47
- **URL**: [https://qiita.com/ennagara128/items/35ce039e95aeaa50bbd7](https://qiita.com/ennagara128/items/35ce039e95aeaa50bbd7)

## 概要

finally(() =&gt; "完了") の戻り値は後続に届きません。一方、例外は元のエラーを置き換えます。
AIにローディング解除を頼んだコードでは、finally() と then() の違いを確認したいところです。
macOS 27.2.1、Node.js v24.22...

---

*この記事は自動収集システムによって保存されました。*
