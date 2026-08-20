---
title: "Claude Code の PostToolUse hook で編集直後に lint・型チェックを自動実行して Claude に差し戻す実装 ― matcher と exit code 2 の3つのハマりどころ【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-08-20T23:03:16
url: https://qiita.com/yureki_lab/items/1128ae4040a191df4e68
---

# Claude Code の PostToolUse hook で編集直後に lint・型チェックを自動実行して Claude に差し戻す実装 ― matcher と exit code 2 の3つのハマりどころ【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年08月20日 23:03
- **URL**: [https://qiita.com/yureki_lab/items/1128ae4040a191df4e68](https://qiita.com/yureki_lab/items/1128ae4040a191df4e68)

## 概要

Claude Code に実装を任せていると、生成コードが lint エラーや型エラーを含んだまま次のファイルへ進んでいく。自分の場合、後からまとめて ruff と mypy を回して「20 個エラーが出ている」と分かり、直すのに 30 分かかった。
これを 編集した瞬間に...

---

*この記事は自動収集システムによって保存されました。*
