---
title: "React + Laravel Sanctumで本番だけ419 —— SameSiteではなくドメイン設計が原因だった"
source: "Qiita (React)"
category: "it"
published: 2026-08-10T20:31:16
url: https://qiita.com/tetsumaru-tech/items/17e9273b6458dc471cf8
---

# React + Laravel Sanctumで本番だけ419 —— SameSiteではなくドメイン設計が原因だった

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年08月10日 20:31
- **URL**: [https://qiita.com/tetsumaru-tech/items/17e9273b6458dc471cf8](https://qiita.com/tetsumaru-tech/items/17e9273b6458dc471cf8)

## 概要

1. 結論
React（TypeScript）+ Laravel Sanctum の SPA 認証で、ローカルではログインできるのに本番だけ POST /api/login が 419 を返しました。
最初に疑ったのは Cookie の SameSite 属性でしたが、こ...

---

*この記事は自動収集システムによって保存されました。*
