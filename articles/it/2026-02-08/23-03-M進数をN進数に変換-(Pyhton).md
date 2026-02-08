---
title: "M進数をN進数に変換 (Pyhton)"
source: "Qiita (Python)"
category: "it"
published: 2026-02-08T23:03:29
url: https://qiita.com/ZawaP/items/9803dcc6457a1303feed
---

# M進数をN進数に変換 (Pyhton)

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年02月08日 23:03
- **URL**: [https://qiita.com/ZawaP/items/9803dcc6457a1303feed](https://qiita.com/ZawaP/items/9803dcc6457a1303feed)

## 概要

少し詰まったので、メモとして残しておきます。

考え方
int で一度10進数に戻してからN進数への変換計算を行う。
def convert_base(m, a, n):
    decimal_val = int(str(a), m)

    if decimal_va...

---

*この記事は自動収集システムによって保存されました。*
