---
title: "【JavaScript正規表現】`(?=.*[a-z])`って何？肯定先読みと`.*`を分解して理解する"
source: "Qiita (React)"
category: "it"
published: 2026-09-02T13:33:46
url: https://qiita.com/windingroad_engineer/items/f4d6c6e80bfb1aaca138
---

# 【JavaScript正規表現】`(?=.*[a-z])`って何？肯定先読みと`.*`を分解して理解する

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年09月02日 13:33
- **URL**: [https://qiita.com/windingroad_engineer/items/f4d6c6e80bfb1aaca138](https://qiita.com/windingroad_engineer/items/f4d6c6e80bfb1aaca138)

## 概要

パスワードのバリデーションなどで、こんな正規表現を見かけることがあります。
/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])/

最初に見たとき、特に分からなかったのが、
(?=.*[a-z])

の部分でした。
「.*は0文字以上なのに、どうして小文...

---

*この記事は自動収集システムによって保存されました。*
