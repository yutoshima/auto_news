---
title: "Preview環境でPRごとに専用DBを使えるようにした話"
source: "Zenn"
category: "it"
published: 2026-07-01T03:00:19
url: https://zenn.dev/estie/articles/59ec0ae59c3199
---

# Preview環境でPRごとに専用DBを使えるようにした話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月01日 03:00
- **URL**: [https://zenn.dev/estie/articles/59ec0ae59c3199](https://zenn.dev/estie/articles/59ec0ae59c3199)

## 概要

こんにちは、株式会社estie（エスティ）でソフトウェアエンジニアをしている木村です。
以前、弊社の徳原が Preview環境の実装について紹介する記事 を書きました。PRごとに専用URLが発行され、変更内容を実際に動かして確認できる仕組みです。
Preview環境は導入してから社内でとても日常的に使われるようになりました。この記事ではまずその使われ方を紹介したうえで、「あと少しだけ届かない」場面を解決するために作ったDB付きPreviewについて書きます。

 Preview環境の社内での使われ方
estieでは10以上のプロダクト、そしてそれらを支える基盤を開発しています。Previ...

---

*この記事は自動収集システムによって保存されました。*
