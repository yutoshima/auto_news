---
title: "Testing Library で "Unable to find role='listitem'" が発生した原因は Zod の UUID 検証だった"
source: "Qiita (React)"
category: "it"
published: 2026-07-12T08:33:12
url: https://qiita.com/kishimin/items/bfa55e489c5b239b2fd1
---

# Testing Library で "Unable to find role='listitem'" が発生した原因は Zod の UUID 検証だった

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年07月12日 08:33
- **URL**: [https://qiita.com/kishimin/items/bfa55e489c5b239b2fd1](https://qiita.com/kishimin/items/bfa55e489c5b239b2fd1)

## 概要

やりたいこと
API 通信後に取得した一覧データのタイトルが表示されることをテストする。

実行したコード
test("タイトルが表示される", async () =&gt; {
  setup();

  const items = await screen.findAllB...

---

*この記事は自動収集システムによって保存されました。*
