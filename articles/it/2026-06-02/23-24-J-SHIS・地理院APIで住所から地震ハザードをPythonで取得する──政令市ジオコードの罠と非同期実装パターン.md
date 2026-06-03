---
title: "J-SHIS・地理院APIで住所から地震ハザードをPythonで取得する──政令市ジオコードの罠と非同期実装パターン"
source: "Qiita (Python)"
category: "it"
published: 2026-06-02T23:24:50
url: https://qiita.com/sakutto-panda/items/5d4525c715468355271b
---

# J-SHIS・地理院APIで住所から地震ハザードをPythonで取得する──政令市ジオコードの罠と非同期実装パターン

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年06月02日 23:24
- **URL**: [https://qiita.com/sakutto-panda/items/5d4525c715468355271b](https://qiita.com/sakutto-panda/items/5d4525c715468355271b)

## 概要

住所から地震リスクを取得する処理を実装した。使うAPIは地理院の住所検索APIとJ-SHISの地震ハザードステーションAPI。どちらも申請不要・APIキーなしで使えるが、ドキュメントに書いてないことが多くて実測で確認しながら進めることになった。

全体の流れ
住所文字列（例...

---

*この記事は自動収集システムによって保存されました。*
