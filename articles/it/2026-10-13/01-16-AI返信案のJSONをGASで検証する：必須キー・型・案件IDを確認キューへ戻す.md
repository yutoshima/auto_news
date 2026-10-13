---
title: "AI返信案のJSONをGASで検証する：必須キー・型・案件IDを確認キューへ戻す"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-13T01:16:44
url: https://qiita.com/Miraigent/items/dbd9f84a5ce048bd0358
---

# AI返信案のJSONをGASで検証する：必須キー・型・案件IDを確認キューへ戻す

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 01:16
- **URL**: [https://qiita.com/Miraigent/items/dbd9f84a5ce048bd0358](https://qiita.com/Miraigent/items/dbd9f84a5ce048bd0358)

## 概要

AIに問い合わせの要約や返信案を作らせると、JSONで受け取る設計は扱いやすく見えます。しかし、JSON.parse()が成功しただけでは、業務データとして受け入れてよいとは限りません。
配列が返る、必須キーが欠ける、予定外の approved が混ざる、呼び出し元とは別の...

---

*この記事は自動収集システムによって保存されました。*
