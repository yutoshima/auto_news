---
title: "Playwright の locator.click() は、メインスレッドが空くまで押しません。反応の遅れを測るときは page.mouse.click() で押します"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-22T01:21:24
url: https://qiita.com/Rapls/items/91dad1bd8b9d5ad81944
---

# Playwright の locator.click() は、メインスレッドが空くまで押しません。反応の遅れを測るときは page.mouse.click() で押します

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月22日 01:21
- **URL**: [https://qiita.com/Rapls/items/91dad1bd8b9d5ad81944](https://qiita.com/Rapls/items/91dad1bd8b9d5ad81944)

## 概要

Playwright で「ページを開いてすぐ、2回続けて押したときの反応の遅れ」を測ろうとして、locator.click() で押すと、遅れが出てきません。
メインスレッドが長いタスクでふさがれているあいだ、locator.click() は押すのを待つからです。押したと...

---

*この記事は自動収集システムによって保存されました。*
