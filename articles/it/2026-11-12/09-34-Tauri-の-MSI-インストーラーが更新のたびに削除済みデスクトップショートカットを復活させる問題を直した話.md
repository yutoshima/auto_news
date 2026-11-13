---
title: "Tauri の MSI インストーラーが更新のたびに削除済みデスクトップショートカットを復活させる問題を直した話"
source: "Zenn"
category: "it"
published: 2026-11-12T09:34:34
url: https://zenn.dev/takahiro_nago/articles/article-tauri-msi-desktop-shortcut
---

# Tauri の MSI インストーラーが更新のたびに削除済みデスクトップショートカットを復活させる問題を直した話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月12日 09:34
- **URL**: [https://zenn.dev/takahiro_nago/articles/article-tauri-msi-desktop-shortcut](https://zenn.dev/takahiro_nago/articles/article-tauri-msi-desktop-shortcut)

## 概要

はじめに
Tauri の MSI インストーラーには、「ユーザーがデスクトップショートカットを削除しても、アプリを更新するたびに復活する」という問題がありました。NSIS 版のインストーラーでは起きない、MSI 版だけの挙動です。
この問題を tauri-bundler 側で修正し、Pull Request が 2026 年 11 月 12 日に dev ブランチへマージされました。この記事では、問題の原因、WiX (Windows Installer XML) のアップグレードの仕組み、修正の中身、そしてレビューで指摘された「この修正では直らないこと」について書きます。

Issu...

---

*この記事は自動収集システムによって保存されました。*
