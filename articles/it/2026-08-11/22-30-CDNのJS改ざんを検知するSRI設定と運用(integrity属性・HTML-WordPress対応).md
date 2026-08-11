---
title: "CDNのJS改ざんを検知するSRI設定と運用(integrity属性・HTML/WordPress対応)"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-11T22:30:00
url: https://qiita.com/jiis-sasaki/items/b9af6a365db98ad95d9d
---

# CDNのJS改ざんを検知するSRI設定と運用(integrity属性・HTML/WordPress対応)

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月11日 22:30
- **URL**: [https://qiita.com/jiis-sasaki/items/b9af6a365db98ad95d9d](https://qiita.com/jiis-sasaki/items/b9af6a365db98ad95d9d)

## 概要

外部のCDNから読み込んでいるJavaScriptやCSSは、自分のサーバーには一切手を加えなくても、配信元が書き換わればそのまま実行されてしまいます。2024年のpolyfill.io事件では、CDN(コンテンツ配信ネットワーク=世界中のサーバーからファイルを配る仕組み)...

---

*この記事は自動収集システムによって保存されました。*
