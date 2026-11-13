---
title: "SQLiteの database is locked をPythonで踏む5つの落とし穴｜timeout・読んでから書く・commit忘れ・WAL・WAL肥大"
source: "Qiita (Python)"
category: "it"
published: 2026-11-13T01:20:12
url: https://qiita.com/cauchye_asia/items/3cb1ad651ea946dfaab3
---

# SQLiteの database is locked をPythonで踏む5つの落とし穴｜timeout・読んでから書く・commit忘れ・WAL・WAL肥大

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月13日 01:20
- **URL**: [https://qiita.com/cauchye_asia/items/3cb1ad651ea946dfaab3](https://qiita.com/cauchye_asia/items/3cb1ad651ea946dfaab3)

## 概要

TL;DR

database is locked は、「別の接続が書き込み中」のときに出ます。sqlite3.connect() の timeout は既定5秒で、その間だけ待ってから失敗します。

BEGIN（DEFERRED）で読んでから書くと、待たずに即失敗する...

---

*この記事は自動収集システムによって保存されました。*
