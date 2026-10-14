---
title: "Cloudflareの_headersが「1行2000文字」上限で落ちた（CSPハッシュ列挙の原因と対処）"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-14T01:13:25
url: https://qiita.com/kusarikakemron/items/542488f29a799f2ce96e
---

# Cloudflareの_headersが「1行2000文字」上限で落ちた（CSPハッシュ列挙の原因と対処）

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 01:13
- **URL**: [https://qiita.com/kusarikakemron/items/542488f29a799f2ce96e](https://qiita.com/kusarikakemron/items/542488f29a799f2ce96e)

## 概要

自社サイトで wrangler deploy を実行したところ、Cloudflare の _headers にある「1行2000文字」の上限に引っかかってデプロイが止まりました。
原因は CSP の script-src に並べていたインラインscriptの sha256 ...

---

*この記事は自動収集システムによって保存されました。*
