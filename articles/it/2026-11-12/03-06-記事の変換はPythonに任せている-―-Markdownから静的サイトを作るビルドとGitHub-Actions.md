---
title: "記事の変換はPythonに任せている ― Markdownから静的サイトを作るビルドとGitHub Actions"
source: "Qiita (Python)"
category: "it"
published: 2026-11-12T03:06:08
url: https://qiita.com/oosawak@github/items/2a811a01c0e0e4695665
---

# 記事の変換はPythonに任せている ― Markdownから静的サイトを作るビルドとGitHub Actions

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月12日 03:06
- **URL**: [https://qiita.com/oosawak@github/items/2a811a01c0e0e4695665](https://qiita.com/oosawak@github/items/2a811a01c0e0e4695665)

## 概要

はじめに
私のサイトは、記事の Markdown を push すると更新されます。
その裏側で動いている変換は、全部 Python です。
ビルドスクリプトは1ファイル（scripts/build.py）で、実行は GitHub Actions に任せています。
この記...

---

*この記事は自動収集システムによって保存されました。*
