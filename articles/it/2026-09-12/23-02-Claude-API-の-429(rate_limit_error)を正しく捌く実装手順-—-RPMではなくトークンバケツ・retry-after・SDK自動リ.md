---
title: "Claude API の 429(rate_limit_error)を正しく捌く実装手順 — RPMではなくトークンバケツ・retry-after・SDK自動リトライの3つのハマりどころ【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-09-12T23:02:12
url: https://qiita.com/yureki_lab/items/b2b0a91c77555f4ff020
---

# Claude API の 429(rate_limit_error)を正しく捌く実装手順 — RPMではなくトークンバケツ・retry-after・SDK自動リトライの3つのハマりどころ【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月12日 23:02
- **URL**: [https://qiita.com/yureki_lab/items/b2b0a91c77555f4ff020](https://qiita.com/yureki_lab/items/b2b0a91c77555f4ff020)

## 概要

はじめに / 対象と前提
Claude API を叩くバッチ処理を書いていたら、途中から 429 rate_limit_error を連発して止まった。リクエスト数は毎分 20 回程度でレート制限(RPM)には全然届いていないはずなのに、なぜか 429 が返る。調べたら ...

---

*この記事は自動収集システムによって保存されました。*
