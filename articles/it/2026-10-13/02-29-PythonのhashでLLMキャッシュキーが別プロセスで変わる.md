---
title: "PythonのhashでLLMキャッシュキーが別プロセスで変わる"
source: "Qiita (Python)"
category: "it"
published: 2026-10-13T02:29:28
url: https://qiita.com/hironakamura_ai/items/bf1a562da1b91529c3cd
---

# PythonのhashでLLMキャッシュキーが別プロセスで変わる

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 02:29
- **URL**: [https://qiita.com/hironakamura_ai/items/bf1a562da1b91529c3cd](https://qiita.com/hironakamura_ai/items/bf1a562da1b91529c3cd)

## 概要

同じ文字列なら同じハッシュ値、と思っていた。自分はLLMのキャッシュキーを確かめていて、別プロセスに同じJSONを渡したらhash()の一致判定がFalseになった。永続キャッシュの空振り。
ディスクやRedisに残すキーには、入力を決まった形式でJSON化し、SHA-25...

---

*この記事は自動収集システムによって保存されました。*
