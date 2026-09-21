---
title: "jev-lint: コード中の命名やコメントが嘘になってないかを高速に確認"
source: "Zenn"
category: "it"
published: 2026-09-19T15:39:57
url: https://zenn.dev/mizchi/articles/jev-lint-intro
---

# jev-lint: コード中の命名やコメントが嘘になってないかを高速に確認

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月19日 15:39
- **URL**: [https://zenn.dev/mizchi/articles/jev-lint-intro](https://zenn.dev/mizchi/articles/jev-lint-intro)

## 概要

jev-lint とは
気づいたら関数名が実態とズレていたり、昔書いたテストケース名やコメントが嘘になっていた、という問題に遭遇したことはありませんか？
それに対して、jev-lint というツールを作りました。
https://github.com/mizchi/jev-lint
詳細はリポジトリ内の skill を AI に読ませればわかると思いますが、 npx -y jev-lint で動きます。

 jev-lint の中身
中身は、ast-grep のセレクタで抽出されたコードに対して、自然言語で書いたルールで、jev でバッチ化してスコアを評価します。
たとえば、関数名が...

---

*この記事は自動収集システムによって保存されました。*
