---
title: "CSVの書き出しで余分なCRを付けないためにnewlineを分けて考える"
source: "Qiita (Python)"
category: "it"
published: 2026-11-26T04:15:54
url: https://qiita.com/szaxstom/items/2ff4008e5f1f528e775c
---

# CSVの書き出しで余分なCRを付けないためにnewlineを分けて考える

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月26日 04:15
- **URL**: [https://qiita.com/szaxstom/items/2ff4008e5f1f528e775c](https://qiita.com/szaxstom/items/2ff4008e5f1f528e775c)

## 概要

在庫CSVを書き出したあと、別のツールで空行が増えたように見える場合があります。CSVライターの行区切りと、テキストストリームの改行変換を両方確認してください。ライターがCRLFを出力した後に、ストリームがLFをさらにCRLFへ変換すると、CRが重なる場合があります。

フ...

---

*この記事は自動収集システムによって保存されました。*
