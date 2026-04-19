---
title: "GuiguiとGhosttyを組み合わせてターミナルGUIを作ってみた"
source: "Zenn"
category: "it"
published: 2026-04-19T03:44:11
url: https://zenn.dev/rinrin_yuuki/articles/448d45e7df01ee
---

# GuiguiとGhosttyを組み合わせてターミナルGUIを作ってみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月19日 03:44
- **URL**: [https://zenn.dev/rinrin_yuuki/articles/448d45e7df01ee](https://zenn.dev/rinrin_yuuki/articles/448d45e7df01ee)

## 概要

はじめに
こんにちは、rin2yhです！
先日のEbitengineぷちconfでhoshiさんの基調講演やLTを聴き、GoでGUIアプリを書いてみたくなりました。題材にはターミナルの自作を選んでいます。Goからlibghostty[1]（Ghosttyのターミナルエンジン）を呼び出して動かせるのかを、併せて検証したかったためです。
結果、macOSで動くシンプルなターミナルが手元で動いています。「Go言語でGhosttyを作る」意味を込めて gostty と名付けています。本記事では、gosttyの実装で発生した問題と、Claude Codeを活用する上で工夫した点を紹介します。
...

---

*この記事は自動収集システムによって保存されました。*
