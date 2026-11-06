---
title: "Slurm は Kaggle で役に立つ"
source: "Zenn"
category: "it"
published: 2026-11-05T11:54:56
url: https://zenn.dev/pomcho555/articles/c455d086ec47af
---

# Slurm は Kaggle で役に立つ

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 11:54
- **URL**: [https://zenn.dev/pomcho555/articles/c455d086ec47af](https://zenn.dev/pomcho555/articles/c455d086ec47af)

## 概要

1. はじめに
Slurm は、スパコンや研究室の GPU クラスタでよく使われるジョブスケジューラです。投入されたジョブをキューに並べておいて、CPU・メモリ・GPU が空いたものから順に実行してくれます。
「大きなクラスタのための道具でしょ？」という印象がありますが、実は自宅の GPU 1 枚で Kaggle をするときにも、めちゃくちゃ役に立ちました！Kaggle の RSNA Knee Abnormality Detection（膝 MRI の異常検出）に RTX 3090 1 枚で参加したとき、学習ジョブの管理に Slurm を使っていたんです。41 日間で、RSNA の学...

---

*この記事は自動収集システムによって保存されました。*
