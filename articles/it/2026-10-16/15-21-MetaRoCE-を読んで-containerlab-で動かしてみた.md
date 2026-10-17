---
title: "MetaRoCE を読んで containerlab で動かしてみた"
source: "Zenn"
category: "it"
published: 2026-10-16T15:21:30
url: https://zenn.dev/nanakanok/articles/b345cea4338851
---

# MetaRoCE を読んで containerlab で動かしてみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月16日 15:21
- **URL**: [https://zenn.dev/nanakanok/articles/b345cea4338851](https://zenn.dev/nanakanok/articles/b345cea4338851)

## 概要

!
MetaRoCE の仕様 v1.0 は 2026 年 10 月に公開されたばかりです。この記事は、仕様と参照実装を読んだうえで、ソフトウェア実装（libsoftmetaroce）を containerlab 上で動かし、プロトコルの仕組みがどう振る舞うかを確かめた個人の検証記録です。ラインレートでの性能評価ではありません。仕様の解釈には誤りが含まれる可能性があります。正確な記述は必ず原典の仕様を参照してください。


 はじめに
AI 学習用のバックエンドネットワークでは、長らく RoCEv2 が使われてきました。ただし RoCEv2 は、PFC で lossless にしたファブリ...

---

*この記事は自動収集システムによって保存されました。*
