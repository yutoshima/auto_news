---
title: "Pythonのsubprocessがタイムアウトしても子プロセスが残る｜shell=True・パイプ待ち・setsid＋ダブルフォークの限界"
source: "Qiita (Python)"
category: "it"
published: 2026-11-03T03:16:43
url: https://qiita.com/cauchye_asia/items/1b61a324fa4f533ea169
---

# Pythonのsubprocessがタイムアウトしても子プロセスが残る｜shell=True・パイプ待ち・setsid＋ダブルフォークの限界

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 03:16
- **URL**: [https://qiita.com/cauchye_asia/items/1b61a324fa4f533ea169](https://qiita.com/cauchye_asia/items/1b61a324fa4f533ea169)

## 概要

TL;DR

この環境では、subprocess.run("...", shell=True, timeout=1) は1.0秒で TimeoutExpired を出しました。しかし止まったのはシェルだけで、孫の sleep が1件残りました。

kill() のあとに ...

---

*この記事は自動収集システムによって保存されました。*
