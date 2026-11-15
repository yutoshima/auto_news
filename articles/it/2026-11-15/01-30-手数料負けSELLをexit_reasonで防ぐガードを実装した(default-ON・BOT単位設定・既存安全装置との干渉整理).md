---
title: "手数料負けSELLをexit_reasonで防ぐガードを実装した(default ON・BOT単位設定・既存安全装置との干渉整理)"
source: "Qiita (Python)"
category: "it"
published: 2026-11-15T01:30:24
url: https://qiita.com/ponfreelance/items/fefd3d8f6299eb6e9986
---

# 手数料負けSELLをexit_reasonで防ぐガードを実装した(default ON・BOT単位設定・既存安全装置との干渉整理)

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 01:30
- **URL**: [https://qiita.com/ponfreelance/items/fefd3d8f6299eb6e9986](https://qiita.com/ponfreelance/items/fefd3d8f6299eb6e9986)

## 概要

自動売買BOTでは、戦略シグナルによるSELLが「約定しても手数料で赤字」になることがあります。この記事では AutoTrader の設計メモとテストの記述をもとに、Signal.exit_reason を強制出口の意思表示として扱う手数料負けガードの考え方、リスクゲートと...

---

*この記事は自動収集システムによって保存されました。*
