---
title: "手書き Provider 261 件を @riverpod へ全面移行した進め方"
source: "Zenn"
category: "it"
published: 2026-11-05T08:07:39
url: https://zenn.dev/jtcc/articles/riverpod-generator-migration
---

# 手書き Provider 261 件を @riverpod へ全面移行した進め方

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月05日 08:07
- **URL**: [https://zenn.dev/jtcc/articles/riverpod-generator-migration](https://zenn.dev/jtcc/articles/riverpod-generator-migration)

## 概要

こんにちは。日本トレカセンターでモバイルアプリを開発している新宅です。
私たちの Flutter アプリで、手書きの Riverpod Provider 宣言 261 件を @riverpod によるコード生成へ全面移行しました。あわせて、Riverpod 3 で非推奨になった StateNotifier を継承するクラス 130 件も、すべて Notifier へ書き換えています。
進め方の軸にしたのは、少数を先に移して難所を確かめ、互いに衝突しない PR に分けることでした。この記事では、数百件の移行をレビュー可能な単位に分けるまでに、何を調べ、どう判断したかを紹介します。
想定読者...

---

*この記事は自動収集システムによって保存されました。*
