---
title: "ハーネスエンジニアリングとループエンジニアリングの違いとは？ aws aidlc workflow kitから整理する"
source: "Zenn"
category: "it"
published: 2026-07-12T05:19:16
url: https://zenn.dev/tacky_exception/articles/4d77fef5a36e42
---

# ハーネスエンジニアリングとループエンジニアリングの違いとは？ aws aidlc workflow kitから整理する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月12日 05:19
- **URL**: [https://zenn.dev/tacky_exception/articles/4d77fef5a36e42](https://zenn.dev/tacky_exception/articles/4d77fef5a36e42)

## 概要

はじめに
最近aidlc-workflowsを利用しています。
導入前は、人間が「関連コードを調べて」「実装して」「ビルドして」「エラーを直して」と、工程ごとに細かく指示を出していました。
kitを使い始めると、AIが最初に計画を作り、既存コードを調査し、実装後にはビルドやテストまで実行してくれるようになりました。エラーが出れば、その結果をもとに修正も試みます。
特に印象的だったのは、比較的安価なモデルでも、以前より安定して実装を進められるようになったことです。
モデル自体が突然賢くなったわけではありません。
では、何が変わったのでしょうか。
kitの構造を改めて見てみると、AIに必...

---

*この記事は自動収集システムによって保存されました。*
