---
title: "`use cache: private` のキャッシュはブラウザに残ることもある"
source: "Zenn"
category: "it"
published: 2026-10-02T04:07:01
url: https://zenn.dev/chot/articles/362b7a2420ef1a
---

# `use cache: private` のキャッシュはブラウザに残ることもある

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月02日 04:07
- **URL**: [https://zenn.dev/chot/articles/362b7a2420ef1a](https://zenn.dev/chot/articles/362b7a2420ef1a)

## 概要

次のように翻訳します。

はじめに
Next.js v16 には use cache: private というディレクティブがあり、cookies() などリクエスト固有の値を読んだ関数の結果をキャッシュできます。その結果がサーバーに残らないということはドキュメントに書かれています。

In production, matching calls within one request can reuse the same result, but Next.js does not store it in a server cache across requests.

日本語訳: プロダクション環境では、同じリクエスト内の一致する呼び出しは同じ結果を再利用できますが、Next.js はリクエストをまたいでサーバーキャッシュにそれを保存しません。

---

*この記事は自動収集システムによって保存されました。*
