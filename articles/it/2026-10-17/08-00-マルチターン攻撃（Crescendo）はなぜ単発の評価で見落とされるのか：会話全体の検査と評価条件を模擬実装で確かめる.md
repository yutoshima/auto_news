---
title: "マルチターン攻撃（Crescendo）はなぜ単発の評価で見落とされるのか：会話全体の検査と評価条件を模擬実装で確かめる"
source: "Qiita (Python)"
category: "it"
published: 2026-10-17T08:00:26
url: https://qiita.com/shalXXXX/items/ed342c5760b9e49d57ce
---

# マルチターン攻撃（Crescendo）はなぜ単発の評価で見落とされるのか：会話全体の検査と評価条件を模擬実装で確かめる

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 08:00
- **URL**: [https://qiita.com/shalXXXX/items/ed342c5760b9e49d57ce](https://qiita.com/shalXXXX/items/ed342c5760b9e49d57ce)

## 概要

LLM のジェイルブレイク評価は、1 回の入力に対してモデルが断るかどうかを見る形が中心です。ところが実際の利用では、ユーザーは何往復も会話を続けられます。無害な質問から始めて少しずつ話を進め、最後にモデル自身の過去の応答を足がかりに目的の出力を引き出すマルチターン攻撃は、...

---

*この記事は自動収集システムによって保存されました。*
