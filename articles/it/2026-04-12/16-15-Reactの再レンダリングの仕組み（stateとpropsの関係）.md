---
title: "Reactの再レンダリングの仕組み（stateとpropsの関係）"
source: "Qiita (React)"
category: "it"
published: 2026-04-12T16:15:06
url: https://qiita.com/ktr_web_dev/items/882309024b5c43dc1118
---

# Reactの再レンダリングの仕組み（stateとpropsの関係）

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年04月12日 16:15
- **URL**: [https://qiita.com/ktr_web_dev/items/882309024b5c43dc1118](https://qiita.com/ktr_web_dev/items/882309024b5c43dc1118)

## 概要

結論
結論としては、実際のトリガーはstate更新であることが多いが、
コンポーネントの視点によってはpropsの変化も再レンダリングのきっかけになる。
親コンポーネント
import { useState } from "react"

function Parent(...

---

*この記事は自動収集システムによって保存されました。*
