---
title: "kintoneの検索クエリに引用符を含む値を渡す｜バックスラッシュとJSONを分けてテストする"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-03T02:09:51
url: https://qiita.com/kintaco/items/5cb8533ee056b80f1d87
---

# kintoneの検索クエリに引用符を含む値を渡す｜バックスラッシュとJSONを分けてテストする

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 02:09
- **URL**: [https://qiita.com/kintaco/items/5cb8533ee056b80f1d87](https://qiita.com/kintaco/items/5cb8533ee056b80f1d87)

## 概要

会社名に " や \ が入っていると、入力値をそのまま連結した検索クエリでは意図した条件を作れません。値をクエリの文字列リテラルへ変換する処理と、リクエストをJSONにする処理を分けます。
この記事では、文字列（1行）フィールドの完全一致条件を作る小さな関数をテストします。...

---

*この記事は自動収集システムによって保存されました。*
