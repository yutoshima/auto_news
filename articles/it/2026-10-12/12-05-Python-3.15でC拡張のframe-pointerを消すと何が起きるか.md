---
title: "Python 3.15でC拡張のframe pointerを消すと何が起きるか"
source: "Qiita (Python)"
category: "it"
published: 2026-10-12T12:05:02
url: https://qiita.com/TechStudioLab/items/5488cd137db8c6ef4719
---

# Python 3.15でC拡張のframe pointerを消すと何が起きるか

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月12日 12:05
- **URL**: [https://qiita.com/TechStudioLab/items/5488cd137db8c6ef4719](https://qiita.com/TechStudioLab/items/5488cd137db8c6ef4719)

## 概要

Python 3.15では、対応プラットフォームでCPythonをframe pointer付きでビルドする方針が採用されました。
しかし、途中のC拡張が-fomit-frame-pointerでビルドされていると、システムプロファイラのスタック追跡は途切れる可能性があり...

---

*この記事は自動収集システムによって保存されました。*
