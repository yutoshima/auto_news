---
title: "Amazon Aurora DSQL の PL/pgSQL で関数とプロシージャを試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T07:13:21
url: https://dev.classmethod.jp/articles/aurora-dsql-plpgsql-functions-procedures/
---

# Amazon Aurora DSQL の PL/pgSQL で関数とプロシージャを試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 07:13
- **URL**: [https://dev.classmethod.jp/articles/aurora-dsql-plpgsql-functions-procedures/](https://dev.classmethod.jp/articles/aurora-dsql-plpgsql-functions-procedures/)

## 概要

Amazon Aurora DSQL で PL/pgSQL がサポートされたので、IF/ELSE・ループ・変数代入で3つのテーブルを更新するプロシージャを作りました。同じ100件の処理を CALL 1回と個別の SQL 文300文で流し、所要時間の短縮を確認できました。

---

*この記事は自動収集システムによって保存されました。*
