---
title: "Cloudflare の CLI を wrangler から cf に移行する"
source: "Zenn"
category: "it"
published: 2026-09-29T04:43:50
url: https://zenn.dev/sora_kumo/articles/cloudflare-to-cf
---

# Cloudflare の CLI を wrangler から cf に移行する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月29日 04:43
- **URL**: [https://zenn.dev/sora_kumo/articles/cloudflare-to-cf](https://zenn.dev/sora_kumo/articles/cloudflare-to-cf)

## 概要

はじめに
Cloudflare から次世代の統合 CLI ツール cf（現在 v1.0.0-beta）が登場しました。
従来の wrangler（wrangler.json / wrangler.jsonc / wrangler.toml）から、TypeScript ベースの型安全な設定ファイル cloudflare.config.ts への移行が推奨されています。
公式には cf migrate という移行コマンドが用意されていますが、実行するだけでそのまま本番稼働できるわけではなく、いくつかの設定調整や実運用上のハマりどころが存在します。
この記事では、React Router（...

---

*この記事は自動収集システムによって保存されました。*
