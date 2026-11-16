---
title: "脱WordPress：10年以上の個人ブログを Astro + Cloudflare Workersへ移行し、PageSpeedを100点に実現"
source: "Zenn"
category: "it"
published: 2026-11-12T15:31:01
url: https://zenn.dev/unsoluble_sugar/articles/8cdf1efc01e6cb
---

# 脱WordPress：10年以上の個人ブログを Astro + Cloudflare Workersへ移行し、PageSpeedを100点に実現

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月12日 15:31
- **URL**: [https://zenn.dev/unsoluble_sugar/articles/8cdf1efc01e6cb](https://zenn.dev/unsoluble_sugar/articles/8cdf1efc01e6cb)

## 概要

はじめに
10 年以上 WordPress で運用してきた個人ブログを Astro + Cloudflare Workers の静的サイト に移行しました。
移行の経緯と読者向けのまとめはブログ側の記事に書いています。
https://unsolublesugar.com/20261112/120000/
この記事では技術的な中身をまとめます。記事データの変換から Cloudflare での公開、公開後の調整までを扱います。作業の大半を Claude に任せた進め方 も紹介します。
!
この記事のポイント

WordPress のエクスポート（WXR）から約 2,000 記事を変換し...

---

*この記事は自動収集システムによって保存されました。*
