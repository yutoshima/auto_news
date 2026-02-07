---
title: "Pythonをアップグレードしたら転送ファイルが0byteになった"
source: "Qiita (Python)"
category: "it"
published: 2026-02-07T08:17:21
url: https://qiita.com/chovin/items/623d506333c30758746f
---

# Pythonをアップグレードしたら転送ファイルが0byteになった

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年02月07日 08:17
- **URL**: [https://qiita.com/chovin/items/623d506333c30758746f](https://qiita.com/chovin/items/623d506333c30758746f)

## 概要

Pythonの継続的なI/Oパフォーマンス改善に伴う内部バッファサイズの拡大により、NamedTemporaryFileへの書き込み直後にファイルパスを外部処理へ渡すと、データがディスクに反映されず「中身が空(0バイト)」として扱われる事象に遭遇。

事象 : 転送ファイル...

---

*この記事は自動収集システムによって保存されました。*
