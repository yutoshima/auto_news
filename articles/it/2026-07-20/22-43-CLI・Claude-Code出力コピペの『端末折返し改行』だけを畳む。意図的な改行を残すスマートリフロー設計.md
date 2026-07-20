---
title: "CLI・Claude Code出力コピペの『端末折返し改行』だけを畳む。意図的な改行を残すスマートリフロー設計"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-20T22:43:09
url: https://qiita.com/sakutto-panda/items/f559ab0b31ebeffd27de
---

# CLI・Claude Code出力コピペの『端末折返し改行』だけを畳む。意図的な改行を残すスマートリフロー設計

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月20日 22:43
- **URL**: [https://qiita.com/sakutto-panda/items/f559ab0b31ebeffd27de](https://qiita.com/sakutto-panda/items/f559ab0b31ebeffd27de)

## 概要

3行まとめ

CLI や Claude Code、PDF からコピペしたテキストの「余計な改行・ノイズ」を掃除するツールを作った
一番難しいのは 端末幅で機械的に折り返された改行だけを畳み、意図的な改行（短い行・体言止め）は残すこと
判定の決め手は 行末の助詞・読点 + ...

---

*この記事は自動収集システムによって保存されました。*
