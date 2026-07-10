---
title: "LLMの返答を画面に出す前の、出力インジェクション対策チェックリスト【WordPressプラグイン】"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-09T23:48:42
url: https://qiita.com/Rapls/items/79151c2e3c94cb9abf12
---

# LLMの返答を画面に出す前の、出力インジェクション対策チェックリスト【WordPressプラグイン】

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月09日 23:48
- **URL**: [https://qiita.com/Rapls/items/79151c2e3c94cb9abf12](https://qiita.com/Rapls/items/79151c2e3c94cb9abf12)

## 概要

先に、いちばん大事な一行を書きます。LLMの返答は、ユーザーが打ち込んだ入力と同じくらい、信用できません。なのに多くの実装は、LLMの出力を「自前で作った安全なデータ」のように扱って、そのまま画面に流し込みます。ここが、出力インジェクションの入口です。
自分は、AIチャット...

---

*この記事は自動収集システムによって保存されました。*
