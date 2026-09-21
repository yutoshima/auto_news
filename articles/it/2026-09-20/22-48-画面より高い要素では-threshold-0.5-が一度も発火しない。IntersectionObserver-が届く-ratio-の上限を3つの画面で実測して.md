---
title: "画面より高い要素では threshold 0.5 が一度も発火しない。IntersectionObserver が届く ratio の上限を3つの画面で実測してみた"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-09-20T22:48:55
url: https://qiita.com/fujiken818/items/8b2e92bc2b70003abdd6
---

# 画面より高い要素では threshold 0.5 が一度も発火しない。IntersectionObserver が届く ratio の上限を3つの画面で実測してみた

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年09月20日 22:48
- **URL**: [https://qiita.com/fujiken818/items/8b2e92bc2b70003abdd6](https://qiita.com/fujiken818/items/8b2e92bc2b70003abdd6)

## 概要

セクションが画面に半分入ったら1回だけイベントを送る、というよくある計測を入れました。素直に new IntersectionObserver(cb, { threshold: 0.5 }) と書いて、手元のPCで動くことを確認して、出しました。
数日後、そのイベントは 0...

---

*この記事は自動収集システムによって保存されました。*
