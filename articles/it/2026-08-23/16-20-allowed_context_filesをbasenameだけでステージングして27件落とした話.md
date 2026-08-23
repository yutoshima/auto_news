---
title: "allowed_context_filesをbasenameだけでステージングして27件落とした話"
source: "Qiita (Python)"
category: "it"
published: 2026-08-23T16:20:10
url: https://qiita.com/SciCos/items/a5a6d516ea4fa0f84520
---

# allowed_context_filesをbasenameだけでステージングして27件落とした話

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月23日 16:20
- **URL**: [https://qiita.com/SciCos/items/a5a6d516ea4fa0f84520](https://qiita.com/SciCos/items/a5a6d516ea4fa0f84520)

## 概要

現象
今週、複数の自律タスクが同じ例外で連続して落ちました。原因はタスクの入力指定そのものではなく、実行前に allowed_context_files を一時ディレクトリへ集める「ステージング」の設計でした。
事故メモには、原因候補として「allowed_context...

---

*この記事は自動収集システムによって保存されました。*
