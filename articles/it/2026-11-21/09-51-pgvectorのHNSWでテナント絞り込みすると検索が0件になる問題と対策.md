---
title: "pgvectorのHNSWでテナント絞り込みすると検索が0件になる問題と対策"
source: "Qiita トレンド"
category: "it"
published: 2026-11-21T09:51:37
url: https://qiita.com/takumi_engineer/items/142ca7088f13f006da82?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items
---

# pgvectorのHNSWでテナント絞り込みすると検索が0件になる問題と対策

## メタデータ

- **情報源**: Qiita トレンド
- **カテゴリ**: it
- **公開日時**: 2026年11月21日 09:51
- **URL**: [https://qiita.com/takumi_engineer/items/142ca7088f13f006da82?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items](https://qiita.com/takumi_engineer/items/142ca7088f13f006da82?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

## 概要

マルチテナントのRAGで、pgvectorのHNSWインデックスに WHERE tenant_id = ... を付けると、LIMITより少ない件数しか返らないことがあります。この記事では、その仕組みと、再現・対策・検知までをコードで示します。
私はマルチテナントのAI業務...

---

*この記事は自動収集システムによって保存されました。*
