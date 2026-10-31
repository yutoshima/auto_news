---
title: "Strict ModeでEffectが二度動く条件を、購読のsetupとcleanupで確認する"
source: "Qiita (React)"
category: "it"
published: 2026-10-30T03:10:30
url: https://qiita.com/hiro123/items/02b3684dd1cd4dec3db6
---

# Strict ModeでEffectが二度動く条件を、購読のsetupとcleanupで確認する

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年10月30日 03:10
- **URL**: [https://qiita.com/hiro123/items/02b3684dd1cd4dec3db6](https://qiita.com/hiro123/items/02b3684dd1cd4dec3db6)

## 概要

Strict ModeでEffectのsetupが2回記録されたときは、間にcleanupがあるかと、最後に残った購読数を確認します。setupの回数だけを1回へ抑えても、後始末ができているとは限りません。
React 19.3.0の開発buildとproduction b...

---

*この記事は自動収集システムによって保存されました。*
