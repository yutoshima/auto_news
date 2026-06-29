---
title: "外部SaaSで運用していたFAQサイトを Cloudflare + Astro に移行しました"
source: "Zenn"
category: "it"
published: 2026-06-29T00:00:27
url: https://zenn.dev/tsukulink/articles/2026-06-faq-astro-migration
---

# 外部SaaSで運用していたFAQサイトを Cloudflare + Astro に移行しました

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月29日 00:00
- **URL**: [https://zenn.dev/tsukulink/articles/2026-06-faq-astro-migration](https://zenn.dev/tsukulink/articles/2026-06-faq-astro-migration)

## 概要

ごきげんよう🙋‍♀️Cloudflareが大好きなあっきー（@kuronekopunk）です。
長らく外部のマネージドなSaaSで運用してきたFAQサイトを、Cloudflare + Astroによる静的サイトへ移行しました。
この記事では技術選定の判断軸と、数百件規模のコンテンツをどう安全に移行したのかを事例として紹介します。
ポイントは次の3つです。

コンテンツをGit管理できるコードベースへ
移行データはエクスポート CSV からスクリプトで安全に移行
新旧サイトを突き合わせる検証スクリプトで安全に切替


 1. なぜ移行したのか
FAQサイトは外部サービスのCRM上で運用して...

---

*この記事は自動収集システムによって保存されました。*
