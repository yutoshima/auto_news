---
title: "ゼロ埋めの slice(-2) は100分を「00分」にする？ padStart との違いと、マイナス・小数・月のずれ"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-13T03:02:51
url: https://qiita.com/ennagara128/items/a9b4e33da93afbe059ef
---

# ゼロ埋めの slice(-2) は100分を「00分」にする？ padStart との違いと、マイナス・小数・月のずれ

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 03:02
- **URL**: [https://qiita.com/ennagara128/items/a9b4e33da93afbe059ef](https://qiita.com/ennagara128/items/a9b4e33da93afbe059ef)

## 概要

時刻を 09:05、番号を No.0007 のように、桁をそろえて表示したい。そんな「ゼロ埋め」には、よく次の2つの書き方が使われます。
const n = 5;
("0" + n).slice(-2);         // "05"
String(n).padStart...

---

*この記事は自動収集システムによって保存されました。*
