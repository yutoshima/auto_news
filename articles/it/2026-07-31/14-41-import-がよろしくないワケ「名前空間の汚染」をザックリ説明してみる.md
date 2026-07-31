---
title: "import * がよろしくないワケ「名前空間の汚染」をザックリ説明してみる"
source: "Qiita (Python)"
category: "it"
published: 2026-07-31T14:41:15
url: https://qiita.com/aKuad/items/860ad5155e313484ca9c
---

# import * がよろしくないワケ「名前空間の汚染」をザックリ説明してみる

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年07月31日 14:41
- **URL**: [https://qiita.com/aKuad/items/860ad5155e313484ca9c](https://qiita.com/aKuad/items/860ad5155e313484ca9c)

## 概要

import * でできること
例えば、標準ライブラリの一つ time 内にある sleep と time を使いたいとして、こんな感じに書くことができます。
from time import *

if __name__ == '__main__':
  print(t...

---

*この記事は自動収集システムによって保存されました。*
