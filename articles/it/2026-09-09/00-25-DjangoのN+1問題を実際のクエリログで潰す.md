---
title: "DjangoのN+1問題を実際のクエリログで潰す"
source: "Qiita (Python)"
category: "it"
published: 2026-09-09T00:25:46
url: https://qiita.com/snowcode_jp/items/583838edc7e2ddac54ae
---

# DjangoのN+1問題を実際のクエリログで潰す

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月09日 00:25
- **URL**: [https://qiita.com/snowcode_jp/items/583838edc7e2ddac54ae](https://qiita.com/snowcode_jp/items/583838edc7e2ddac54ae)

## 概要

DjangoのORMは書きやすい反面、気づかないうちに大量のクエリを発行します。代表格が N+1問題 です。「なんとなく遅い」を、実際のクエリログで特定して潰す 手順を示します。

N+1問題とは
一覧を1回取得（1）したあと、各行の関連データを1件ずつ取得（N回）してしま...

---

*この記事は自動収集システムによって保存されました。*
