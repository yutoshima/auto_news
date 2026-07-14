---
title: "AI時代のObservability設計 - PIIとAIの検索性を両立させ、自動修復する（実践編）"
source: "Zenn"
category: "it"
published: 2026-07-13T23:51:06
url: https://zenn.dev/aircloset/articles/3b8e60fcaab4b7
---

# AI時代のObservability設計 - PIIとAIの検索性を両立させ、自動修復する（実践編）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月13日 23:51
- **URL**: [https://zenn.dev/aircloset/articles/3b8e60fcaab4b7](https://zenn.dev/aircloset/articles/3b8e60fcaab4b7)

## 概要

!
English Version is here

みなさまこんにちは！エアークローゼットでCTOをしている辻です。
設計編では、アプリケーション / インフラ / CI / LLMの4軸を、それぞれの問いの性質に合わせて別々の形でObservableにする話を書きました。ここまでで観測スタックの書き込み側は一旦区切ったところです。
ただし、「Observableにしただけ」で話は終わりません。観測スタックには本番データが流れる以上、ここにPIIが混入する経路を断たないといけない ── これはAIとは無関係に、observability設計で手を抜くと漏洩事故に直結する古典的な問題です...

---

*この記事は自動収集システムによって保存されました。*
