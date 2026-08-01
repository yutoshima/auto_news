---
title: "Markdownテーブルの書き方と生成ツールの実装 — GFM区切り行の配置指定・エスケープ・Reactの状態設計"
source: "Qiita (React)"
category: "it"
published: 2026-08-01T22:41:17
url: https://qiita.com/sakutto-panda/items/41f435c5dbbf3d3d07aa
---

# Markdownテーブルの書き方と生成ツールの実装 — GFM区切り行の配置指定・エスケープ・Reactの状態設計

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年08月01日 22:41
- **URL**: [https://qiita.com/sakutto-panda/items/41f435c5dbbf3d3d07aa](https://qiita.com/sakutto-panda/items/41f435c5dbbf3d3d07aa)

## 概要

3行まとめ

行列数を指定してセルを埋めるだけで、Markdown・HTML・CSV の3形式でテーブルを出力するブラウザ完結ツールを作った
生成ロジックは3つの純粋関数だけ。形式ごとに「エスケープすべき危険文字」が違う（Markdown は |、HTML は &amp; &lt; &gt;...

---

*この記事は自動収集システムによって保存されました。*
