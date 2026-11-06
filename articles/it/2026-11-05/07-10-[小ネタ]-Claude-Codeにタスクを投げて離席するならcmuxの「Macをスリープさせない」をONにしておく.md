---
title: "[小ネタ] Claude Codeにタスクを投げて離席するならcmuxの「Macをスリープさせない」をONにしておく"
source: "DevelopersIO"
category: "it"
published: 2026-11-05T07:10:42
url: https://dev.classmethod.jp/articles/cmux-keep-mac-awake-claude-code-away/
---

# [小ネタ] Claude Codeにタスクを投げて離席するならcmuxの「Macをスリープさせない」をONにしておく

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 07:10
- **URL**: [https://dev.classmethod.jp/articles/cmux-keep-mac-awake-claude-code-away/](https://dev.classmethod.jp/articles/cmux-keep-mac-awake-claude-code-away/)

## 概要

cmuxに追加された「Macをスリープさせない」を調べました。中身はProcessInfo.beginActivityによるアイドルスリープ抑止で、蓋を閉じればスリープします。cmux終了でOFFに戻る点、Claude Codeのcaffeinateだけでは離席中のスリープを防げなかった事例も紹介します。

---

*この記事は自動収集システムによって保存されました。*
