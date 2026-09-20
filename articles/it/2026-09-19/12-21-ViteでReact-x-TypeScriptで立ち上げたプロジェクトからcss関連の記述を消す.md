---
title: "ViteでReact x TypeScriptで立ち上げたプロジェクトからcss関連の記述を消す"
source: "Qiita (React)"
category: "it"
published: 2026-09-19T12:21:00
url: https://qiita.com/J-T_ky2g/items/5e2bf2bf02e589e225d3
---

# ViteでReact x TypeScriptで立ち上げたプロジェクトからcss関連の記述を消す

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年09月19日 12:21
- **URL**: [https://qiita.com/J-T_ky2g/items/5e2bf2bf02e589e225d3](https://qiita.com/J-T_ky2g/items/5e2bf2bf02e589e225d3)

## 概要

はじめに

何度も検証用、練習用にviteプロジェクトを立ち上げている

問題

不要な記述は触りたいファイル内から消すなら手動でいいけど、cssはあっちこっちいくから面倒

解決

以下のコマンドで解決

rm src/App.css
rm src/index.cs...

---

*この記事は自動収集システムによって保存されました。*
