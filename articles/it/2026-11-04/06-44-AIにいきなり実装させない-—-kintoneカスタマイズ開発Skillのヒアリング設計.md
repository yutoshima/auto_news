---
title: "AIにいきなり実装させない — kintoneカスタマイズ開発Skillのヒアリング設計"
source: "Zenn"
category: "it"
published: 2026-11-04T06:44:57
url: https://zenn.dev/genda_jp/articles/a5cbba3664748b
---

# AIにいきなり実装させない — kintoneカスタマイズ開発Skillのヒアリング設計

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月04日 06:44
- **URL**: [https://zenn.dev/genda_jp/articles/a5cbba3664748b](https://zenn.dev/genda_jp/articles/a5cbba3664748b)

## 概要

こんにちは、IT戦略部の谷川です。
GENDAでは社内の業務アプリの一部をkintoneで構築しており、標準機能で足りない部分をkintoneのJavaScriptのカスタマイズで補っています。しかし要望が出るたびにコードを書くことになるので、この部分をAIに任せられないかと考え、ClaudeのAgent Skillsで仕組み化しました。要件のヒアリングから実装、GitHub経由でkintoneへ適用するところまでをこのSkillが担います。
Skillを設計していて一番重要だと感じたのは、実装のさせ方ではなく、実装に着手する前に何を確定させておくかという点でした。
本記事では、作成した...

---

*この記事は自動収集システムによって保存されました。*
