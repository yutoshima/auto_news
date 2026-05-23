---
title: "useEffect は、クリーンアップに使用される関数以外の値を返してはいけません。"
source: "Qiita (React)"
category: "it"
published: 2026-05-22T13:54:32
url: https://qiita.com/o68606007/items/c73aeb1cd173e641328a
---

# useEffect は、クリーンアップに使用される関数以外の値を返してはいけません。

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年05月22日 13:54
- **URL**: [https://qiita.com/o68606007/items/c73aeb1cd173e641328a](https://qiita.com/o68606007/items/c73aeb1cd173e641328a)

## 概要

はじめに
アプリ開発中に、useEffectのデータ取得でエラーが起きました。

問題
useEffectからデータ取得しているにも関わらずエラーが起こりました。

Home
import { useAuthContext } from "../context/AuthC...

---

*この記事は自動収集システムによって保存されました。*
