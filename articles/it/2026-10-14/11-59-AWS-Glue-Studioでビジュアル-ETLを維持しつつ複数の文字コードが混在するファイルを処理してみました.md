---
title: "AWS Glue Studioでビジュアル ETLを維持しつつ複数の文字コードが混在するファイルを処理してみました"
source: "DevelopersIO"
category: "it"
published: 2026-10-14T11:59:44
url: https://dev.classmethod.jp/articles/glue-studio-mix-char-code-transform/
---

# AWS Glue Studioでビジュアル ETLを維持しつつ複数の文字コードが混在するファイルを処理してみました

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 11:59
- **URL**: [https://dev.classmethod.jp/articles/glue-studio-mix-char-code-transform/](https://dev.classmethod.jp/articles/glue-studio-mix-char-code-transform/)

## 概要

AWS Glue StudioではビジュアルETLを利用することでGUIでの直感的なETLの構築を実現可能ですが、Glueの特性として処理するファイルはUTF-8が前提であり異なる文字コードは直接対応していません。今回は任意のスクリプトを部分的に埋め込めるCustom Transformを利用して文字コードが混在したファイルを処理してみました。

---

*この記事は自動収集システムによって保存されました。*
