---
title: "TSRSを導入したら OxLint の type-aware linting と typecheck が爆速になった話"
source: "Zenn"
category: "it"
published: 2026-11-18T07:00:06
url: https://zenn.dev/dress_code/articles/6c179ae5129131
---

# TSRSを導入したら OxLint の type-aware linting と typecheck が爆速になった話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月18日 07:00
- **URL**: [https://zenn.dev/dress_code/articles/6c179ae5129131](https://zenn.dev/dress_code/articles/6c179ae5129131)

## 概要

はじめに
こんにちは。ぷーじ（@yug1224）です。
以前の記事で、フロントエンドとバックエンドに oxlint、oxfmt、tsgo を入れた話を書きました。
https://zenn.dev/dress_code/articles/d655cd7a43b936
その後も type-aware linting と typecheck は CI の中で重いステップのままで、キャッシュが外れるとバックエンドの typecheck だけで 4 分以上かかっていました。
2026 年 11 月 17 日に、oxlint の type-aware linting で tsrs を使えるよ...

---

*この記事は自動収集システムによって保存されました。*
