---
title: "OpenSearchのLLM-as-a-Judgeを日本語の商品検索で動かして、人手ラベルと比べてみた"
source: "Zenn"
category: "it"
published: 2026-10-29T02:55:28
url: https://zenn.dev/nextbeat/articles/c22b45b1d784b0
---

# OpenSearchのLLM-as-a-Judgeを日本語の商品検索で動かして、人手ラベルと比べてみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月29日 02:55
- **URL**: [https://zenn.dev/nextbeat/articles/c22b45b1d784b0](https://zenn.dev/nextbeat/articles/c22b45b1d784b0)

## 概要

はじめに
Search Relevance Workbench（SRW）は、OpenSearch 3.1で導入された検索品質を評価するための機能です。クエリと検索設定、正解データを組み合わせてNDCGなどの指標を計算できます。正解データは自分で用意するのが一般的ですが、SRWにはLLMに検索結果の関連度を採点させて正解データを作る、LLM-as-a-Judgeという機能も用意されています。
英語の紹介記事はありましたが、日本語のデータで試した例は見当たらなかったので、今回はAmazonの商品検索データセット（ESCI）の日本語データを使って実際に動かしてみました。ESCIには人が付け...

---

*この記事は自動収集システムによって保存されました。*
