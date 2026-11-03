---
title: "PythonとSQLiteで二重取込を防ぐ、変更行は止める"
source: "Qiita (Python)"
category: "it"
published: 2026-11-03T03:28:43
url: https://qiita.com/eiri_ai/items/256acf543e2dab111afb
---

# PythonとSQLiteで二重取込を防ぐ、変更行は止める

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 03:28
- **URL**: [https://qiita.com/eiri_ai/items/256acf543e2dab111afb](https://qiita.com/eiri_ai/items/256acf543e2dab111afb)

## 概要

ターミナルで同じ取込を2回動かす。1回目は1件登録、2回目は0件。ここまでは順調でした。ところが、同じ受注IDの金額を変えても、エラーなしで0件になった。
「重複したら無視する」だけの処理を、僕は業務の取込には使いたくありません。再実行で増やさないことと、訂正データを握りつ...

---

*この記事は自動収集システムによって保存されました。*
