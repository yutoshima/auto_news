---
title: "SQLite FTS5で件数は1件、検索は0件になる理由"
source: "Qiita (Python)"
category: "it"
published: 2026-11-06T02:26:18
url: https://qiita.com/hironakamura_ai/items/d1e10eb006ebeee5e281
---

# SQLite FTS5で件数は1件、検索は0件になる理由

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月06日 02:26
- **URL**: [https://qiita.com/hironakamura_ai/items/d1e10eb006ebeee5e281](https://qiita.com/hironakamura_ai/items/d1e10eb006ebeee5e281)

## 概要

1件読めるのに、検索すると0件。macOSのCPython 3.14.8、SQLite 3.54.1で確かめた。
自分は今日、RAGの検索用に、既存文書へFTS5を後付けするコードを動かした。本文まで読めるのに、MATCHでは出てこないんだよね。
件数の照合だけで済ませるの...

---

*この記事は自動収集システムによって保存されました。*
