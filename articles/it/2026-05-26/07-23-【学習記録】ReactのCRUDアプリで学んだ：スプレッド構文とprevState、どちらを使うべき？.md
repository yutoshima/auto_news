---
title: "【学習記録】ReactのCRUDアプリで学んだ：スプレッド構文とprevState、どちらを使うべき？"
source: "Qiita (React)"
category: "it"
published: 2026-05-26T07:23:27
url: https://qiita.com/05m/items/8cd806373b64caa1f338
---

# 【学習記録】ReactのCRUDアプリで学んだ：スプレッド構文とprevState、どちらを使うべき？

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年05月26日 07:23
- **URL**: [https://qiita.com/05m/items/8cd806373b64caa1f338](https://qiita.com/05m/items/8cd806373b64caa1f338)

## 概要

ReactでTodoアプリなどのCRUDアプリを作っていると、こんなコードを書く場面が出てきます。
const handleAddTodo = () => {
  setTodos([...todos, { id: todoId, title: todoTitle }])
...

---

*この記事は自動収集システムによって保存されました。*
