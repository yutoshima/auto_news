---
title: "portless が便利なら、Docker Compose には Traefik がある"
source: "Zenn"
category: "it"
published: 2026-02-27T01:31:53
url: https://zenn.dev/mickamy/articles/9a251e7cf51b9c
---

# portless が便利なら、Docker Compose には Traefik がある

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月27日 01:31
- **URL**: [https://zenn.dev/mickamy/articles/9a251e7cf51b9c](https://zenn.dev/mickamy/articles/9a251e7cf51b9c)

## 概要

portless とは
portless は Vercel Labs が公開したローカル開発ツールで、localhost:3000
のようなポート番号を myapp.localhost:1355 のような名前付き URL に変換してくれます。
portless myapp next dev
# → http://myapp.localhost:1355
もうポート番号を覚える必要はありません。モノレポで複数サービスを立ち上げていても、api.localhost:1355、
frontend.localhost:1355 とアクセスできます。
ただし portless はプロセスを直接...

---

*この記事は自動収集システムによって保存されました。*
