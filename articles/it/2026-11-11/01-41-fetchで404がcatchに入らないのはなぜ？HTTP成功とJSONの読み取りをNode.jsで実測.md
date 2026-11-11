---
title: "fetchで404がcatchに入らないのはなぜ？HTTP成功とJSONの読み取りをNode.jsで実測"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-11T01:41:34
url: https://qiita.com/ennagara128/items/e4339d34ffd414bb25e9
---

# fetchで404がcatchに入らないのはなぜ？HTTP成功とJSONの読み取りをNode.jsで実測

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月11日 01:41
- **URL**: [https://qiita.com/ennagara128/items/e4339d34ffd414bb25e9](https://qiita.com/ennagara128/items/e4339d34ffd414bb25e9)

## 概要

404 でも fetch() の catch に入らないことがあります。
HTTP の成功と JSON の読み取りは別の判定です。
macOS 27.2 / Node.js v24.22.1 のローカル HTTP で実測しました。ブラウザ・CORS・認証・リダイレクトは未検...

---

*この記事は自動収集システムによって保存されました。*
