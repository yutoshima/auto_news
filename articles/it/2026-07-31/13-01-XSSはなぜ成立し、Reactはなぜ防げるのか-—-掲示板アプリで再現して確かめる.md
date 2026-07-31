---
title: "XSSはなぜ成立し、Reactはなぜ防げるのか — 掲示板アプリで再現して確かめる"
source: "Qiita (React)"
category: "it"
published: 2026-07-31T13:01:00
url: https://qiita.com/nakashita-abc/items/425c0bf46fd851502651
---

# XSSはなぜ成立し、Reactはなぜ防げるのか — 掲示板アプリで再現して確かめる

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年07月31日 13:01
- **URL**: [https://qiita.com/nakashita-abc/items/425c0bf46fd851502651](https://qiita.com/nakashita-abc/items/425c0bf46fd851502651)

## 概要

はじめに
機能を実装するとき、意識は「要求どおり動くか」に向きがちで、
「その入力値を攻撃者がどう悪用するか」までは考えが及びにくい。
この記事では、実際に動く掲示板アプリでXSSを再現し、
「なぜ成立するのか」を明確にしたうえで対策する。
最終的に、XSSの本質を一つの...

---

*この記事は自動収集システムによって保存されました。*
