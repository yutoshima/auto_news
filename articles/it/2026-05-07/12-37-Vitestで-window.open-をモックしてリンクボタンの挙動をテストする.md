---
title: "Vitestで window.open をモックしてリンクボタンの挙動をテストする"
source: "Qiita (React)"
category: "it"
published: 2026-05-07T12:37:35
url: https://qiita.com/natsugure/items/4c218af2d302ecd83335
---

# Vitestで window.open をモックしてリンクボタンの挙動をテストする

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年05月07日 12:37
- **URL**: [https://qiita.com/natsugure/items/4c218af2d302ecd83335](https://qiita.com/natsugure/items/4c218af2d302ecd83335)

## 概要

はじめに
「新しいタブでURLを開く」ボタンをテストしようとしたら、window.open が jsdom では動かなくて詰まりました。
jsdom（Vitestのデフォルト環境）はブラウザAPIを完全に実装しているわけではないので、window.open をそのまま呼ぼ...

---

*この記事は自動収集システムによって保存されました。*
