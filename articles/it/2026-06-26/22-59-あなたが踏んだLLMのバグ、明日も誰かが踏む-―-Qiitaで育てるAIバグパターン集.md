---
title: "あなたが踏んだLLMのバグ、明日も誰かが踏む ― Qiitaで育てるAIバグパターン集"
source: "Qiita (Python)"
category: "it"
published: 2026-06-26T22:59:32
url: https://qiita.com/nakatada-lab/items/4715df3bf07050d0ed39
---

# あなたが踏んだLLMのバグ、明日も誰かが踏む ― Qiitaで育てるAIバグパターン集

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年06月26日 22:59
- **URL**: [https://qiita.com/nakatada-lab/items/4715df3bf07050d0ed39](https://qiita.com/nakatada-lab/items/4715df3bf07050d0ed39)

## 概要

まず見てほしい
LLMにこう頼んだ。
pandasでCSVを読み込んで、日付列で古い順にソートして

返ってきたコード。
import pandas as pd

df = pd.read_csv("data.csv")
df = df.sort_values("date...

---

*この記事は自動収集システムによって保存されました。*
