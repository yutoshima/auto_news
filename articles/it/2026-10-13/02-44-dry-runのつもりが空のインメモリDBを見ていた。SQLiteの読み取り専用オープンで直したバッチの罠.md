---
title: "dry-runのつもりが空のインメモリDBを見ていた。SQLiteの読み取り専用オープンで直したバッチの罠"
source: "Qiita (Python)"
category: "it"
published: 2026-10-13T02:44:23
url: https://qiita.com/sakutto-panda/items/570b355eb775d7bdf121
---

# dry-runのつもりが空のインメモリDBを見ていた。SQLiteの読み取り専用オープンで直したバッチの罠

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 02:44
- **URL**: [https://qiita.com/sakutto-panda/items/570b355eb775d7bdf121](https://qiita.com/sakutto-panda/items/570b355eb775d7bdf121)

## 概要

住所や地域ごとに災害リスクを集計するサービスを個人開発していて、月次でデータを更新するETLバッチを回している。このバッチの --dry-run オプションが、実は一度も正しく機能していなかったことに気づいた話を書く。

月次更新バッチの構造
不動産情報ライブラリAPIが提...

---

*この記事は自動収集システムによって保存されました。*
