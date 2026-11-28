---
title: "Playwrightで pushState の呼び出し元を記録し、戻るボタンで元のページに戻れるかを点検する"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-28T03:41:00
url: https://qiita.com/masakazuimai/items/c2193827b43682ea1b95
---

# Playwrightで pushState の呼び出し元を記録し、戻るボタンで元のページに戻れるかを点検する

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月28日 03:41
- **URL**: [https://qiita.com/masakazuimai/items/c2193827b43682ea1b95](https://qiita.com/masakazuimai/items/c2193827b43682ea1b95)

## 概要

広告や計測タグを扱う開発者、SPA（ページを再読み込みせず表示を切り替えるアプリ）の開発者向けです。Playwright（ブラウザ操作の自動化ツール）で一回戻り、戻った URL と pushState（履歴を追加するメソッド）の呼び出し元から修正箇所を絞ります。

実行環境...

---

*この記事は自動収集システムによって保存されました。*
