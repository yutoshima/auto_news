---
title: "XML/HTML整形と文字参照（実体参照・数値文字参照）の落とし穴｜閉じタグ破損やエスケープ漏れを防ぐパースの仕組み"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-19T02:12:55
url: https://qiita.com/t_shamoji/items/c1bfaa21c11b252c8cc9
---

# XML/HTML整形と文字参照（実体参照・数値文字参照）の落とし穴｜閉じタグ破損やエスケープ漏れを防ぐパースの仕組み

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 02:12
- **URL**: [https://qiita.com/t_shamoji/items/c1bfaa21c11b252c8cc9](https://qiita.com/t_shamoji/items/c1bfaa21c11b252c8cc9)

## 概要

はじめに
Web開発やAPI連携、SVG素材の編集をしていると、日常的に以下のような作業が発生します。

圧縮（Minify）されて1行になった巨大な XML や HTML を見やすくインデント整形 したい
ログやフォーム入力から抜いたHTML断片を、&lt; や &gt;、&amp; など...

---

*この記事は自動収集システムによって保存されました。*
