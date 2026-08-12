---
title: "git subtreeで2つのGitリポジトリを履歴ごとモノレポにした後、git log で履歴が追えなくなった話"
source: "Qiita (React)"
category: "it"
published: 2026-08-12T21:08:53
url: https://qiita.com/tetsumaru-tech/items/55deec174d7fcb5fee67
---

# git subtreeで2つのGitリポジトリを履歴ごとモノレポにした後、git log で履歴が追えなくなった話

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年08月12日 21:08
- **URL**: [https://qiita.com/tetsumaru-tech/items/55deec174d7fcb5fee67](https://qiita.com/tetsumaru-tech/items/55deec174d7fcb5fee67)

## 概要

結論
React 製の管理画面と Laravel 製のAPIを、別々のGitリポジトリで管理していました。
これを git subtree で1つのリポジトリ（モノレポ）にまとめました。履歴を捨てずに、--squash なしで統合しています。
作業自体は2分41秒で終わり...

---

*この記事は自動収集システムによって保存されました。*
