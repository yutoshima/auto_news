---
title: "LangGraphのdurability、exitで落ちると再開すらできなかった"
source: "Qiita (Python)"
category: "it"
published: 2026-09-01T00:08:53
url: https://qiita.com/kai_kou/items/cf6a2ef912caf8a6a230
---

# LangGraphのdurability、exitで落ちると再開すらできなかった

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月01日 00:08
- **URL**: [https://qiita.com/kai_kou/items/cf6a2ef912caf8a6a230](https://qiita.com/kai_kou/items/cf6a2ef912caf8a6a230)

## 概要

はじめに
LangGraph のグラフを checkpointer 付きでコンパイルすると、途中でプロセスが落ちても続きから再開できます。ただし「どこまで書き込まれているか」は durability という引数で変わります。対象読者は、LangGraph でエージェントを...

---

*この記事は自動収集システムによって保存されました。*
