---
title: "C# × Oracle ストアドプロシージャ早見表（WinForms の取得・登録・更新・削除・CSV 出力）"
source: "Zenn"
category: "it"
published: 2026-10-25T00:56:37
url: https://zenn.dev/hiroshi00000000/articles/078de5ac61693b
---

# C# × Oracle ストアドプロシージャ早見表（WinForms の取得・登録・更新・削除・CSV 出力）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 00:56
- **URL**: [https://zenn.dev/hiroshi00000000/articles/078de5ac61693b](https://zenn.dev/hiroshi00000000/articles/078de5ac61693b)

## 概要

C# の Windows フォームで Oracle を使う画面を作るたびに調べ直していた「ストアドプロシージャの呼び方」と「取得・登録・更新・削除・CSV 出力の書き方」を、1 ページにまとめました。ストアドが OUT 引数で返す結果コード・メッセージの受け取り方と、エラーになったときの流れも入れています。早見表からやりたいことのコードを見て、表名・列名を書きかえれば、そのまま使えます。
.NET 8 / Windows フォーム / Oracle Database 12c 以降 / ODP.NET（Oracle.ManagedDataAccess.Core）
!
この記事の前提

取得...

---

*この記事は自動収集システムによって保存されました。*
