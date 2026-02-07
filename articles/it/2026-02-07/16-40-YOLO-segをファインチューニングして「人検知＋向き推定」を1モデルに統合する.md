---
title: "YOLO-segをファインチューニングして「人検知＋向き推定」を1モデルに統合する"
source: "Qiita (Python)"
category: "it"
published: 2026-02-07T16:40:57
url: https://qiita.com/kiyokiyomin/items/e800e7b67a12c40d37a9
---

# YOLO-segをファインチューニングして「人検知＋向き推定」を1モデルに統合する

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年02月07日 16:40
- **URL**: [https://qiita.com/kiyokiyomin/items/e800e7b67a12c40d37a9](https://qiita.com/kiyokiyomin/items/e800e7b67a12c40d37a9)

## 概要

今回はYOLO26s-segをファインチューニングして、歩行者セグメンテーションと向き推定を同時に行うモデルを獲得してみました。
ソースコードはこちらです。

背景

従来の構成
研究要件として、歩行者のセグメンテーションと、向き推定（カメラと同じ方向を向いているか否か）が...

---

*この記事は自動収集システムによって保存されました。*
