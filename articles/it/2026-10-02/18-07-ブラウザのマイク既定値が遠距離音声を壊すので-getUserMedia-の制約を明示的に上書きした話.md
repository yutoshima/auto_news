---
title: "ブラウザのマイク既定値が遠距離音声を壊すので getUserMedia の制約を明示的に上書きした話"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-02T18:07:50
url: https://qiita.com/Florian/items/0971839d80dec49694e6
---

# ブラウザのマイク既定値が遠距離音声を壊すので getUserMedia の制約を明示的に上書きした話

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月02日 18:07
- **URL**: [https://qiita.com/Florian/items/0971839d80dec49694e6](https://qiita.com/Florian/items/0971839d80dec49694e6)

## 概要

Web アプリでマイクを取得するとき、getUserMedia({ audio: true }) と書くだけで音は取れる。ただしこの「取れる」は、ブラウザが既定で有効にする音声前処理を全部通った後の音である。ノイズ抑制が代表格で、定常ノイズを推定して引き算する処理が常時かか...

---

*この記事は自動収集システムによって保存されました。*
