---
title: "CSS clamp() で fluid typography を自動計算するツールを作った — 中身の線形補間とアクセシビリティを保つ rem 表現"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-06-05T23:28:16
url: https://qiita.com/sen-ltd/items/419a74a77c6f8f2fea12
---

# CSS clamp() で fluid typography を自動計算するツールを作った — 中身の線形補間とアクセシビリティを保つ rem 表現

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年06月05日 23:28
- **URL**: [https://qiita.com/sen-ltd/items/419a74a77c6f8f2fea12](https://qiita.com/sen-ltd/items/419a74a77c6f8f2fea12)

## 概要

font-size: clamp(1rem, 0.875rem + 0.5vw, 1.5rem) のような Fluid Typography は、もうレスポンシブ実装の標準になっています。メディアクエリなしでビューポートに連動します。ただし「最小 16px、最大 24...」

---

*この記事は自動収集システムによって保存されました。*
