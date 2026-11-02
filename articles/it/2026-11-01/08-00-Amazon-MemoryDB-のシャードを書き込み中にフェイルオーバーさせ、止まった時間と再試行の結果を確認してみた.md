---
title: "Amazon MemoryDB のシャードを書き込み中にフェイルオーバーさせ、止まった時間と再試行の結果を確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-01T08:00:31
url: https://dev.classmethod.jp/articles/memorydb-failover-shard-during-writes-retry/
---

# Amazon MemoryDB のシャードを書き込み中にフェイルオーバーさせ、止まった時間と再試行の結果を確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月01日 08:00
- **URL**: [https://dev.classmethod.jp/articles/memorydb-failover-shard-during-writes-retry/](https://dev.classmethod.jp/articles/memorydb-failover-shard-during-writes-retry/)

## 概要

AWS MemoryDB でプライマリノードのフェイルオーバーが発生したとき、アプリケーションの書き込みが実際に何秒止まるのか、どんなエラーが返されるのか、再試行でデータを取りこぼさないようにするにはどうすればいいのかを、実際に検証してみました。

---

*この記事は自動収集システムによって保存されました。*
