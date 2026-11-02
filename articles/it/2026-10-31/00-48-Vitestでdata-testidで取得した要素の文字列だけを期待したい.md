---
title: "Vitestでdata-testidで取得した要素の文字列だけを期待したい"
source: "Qiita トレンド"
category: "it"
published: 2026-10-31T00:48:15
url: https://qiita.com/J-T_ky2g/items/e6df6e90c887421efeb1?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items
---

# Vitestでdata-testidで取得した要素の文字列だけを期待したい

## メタデータ

- **情報源**: Qiita トレンド
- **カテゴリ**: it
- **公開日時**: 2026年10月31日 00:48
- **URL**: [https://qiita.com/J-T_ky2g/items/e6df6e90c887421efeb1?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items](https://qiita.com/J-T_ky2g/items/e6df6e90c887421efeb1?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

## 概要

はじめに

それらしいマッチャがなかった

問題

domを厳密に比較してしまい落ちる

import { render } from "@testing-library/react";
import { describe, expect, it, vi } from ...

---

*この記事は自動収集システムによって保存されました。*
