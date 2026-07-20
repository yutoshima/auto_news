---
title: "Linuxのディレクトリ配置ルール（FHS）超入門"
source: "Zenn"
category: "it"
published: 2026-07-20T02:18:03
url: https://zenn.dev/juth/articles/9dc12f2621e2c1
---

# Linuxのディレクトリ配置ルール（FHS）超入門

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月20日 02:18
- **URL**: [https://zenn.dev/juth/articles/9dc12f2621e2c1](https://zenn.dev/juth/articles/9dc12f2621e2c1)

## 概要

Linuxサーバーを触っていて、「あれ、PostgreSQLの設定ファイルってどこだっけ？」「アプリのデータってどこに保存されてるの？」と迷ったことはありませんか？
実は、Linuxの世界には　「どのファイルはどこに配置する」という世界共通の厳格なルール　があります。このルールのことを FHS（Filesystem Hierarchy Standard） と呼びます。
今回は、初心者向けに「なぜその場所にファイルがあるのか」が直感的にわかるよう、Windowsの概念に例えながら基本のディレクトリ構造をまとめました。


 📂 Linux基本ディレクトリ配置ルール一覧
Linuxサーバーを...

---

*この記事は自動収集システムによって保存されました。*
