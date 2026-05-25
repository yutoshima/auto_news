---
title: "AIエージェントからJPYCを送る: EIP-3009が使えなかった話とSpending Policyの実装"
source: "Zenn"
category: "it"
published: 2026-05-24T00:25:05
url: https://zenn.dev/k0yote/articles/0998c7c7f22ba9
---

# AIエージェントからJPYCを送る: EIP-3009が使えなかった話とSpending Policyの実装

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月24日 00:25
- **URL**: [https://zenn.dev/k0yote/articles/0998c7c7f22ba9](https://zenn.dev/k0yote/articles/0998c7c7f22ba9)

## 概要

!
シリーズ: AIエージェント向けStablecoin SDKを6ヶ月で公開する記録 (2/X)
前回 (#1) は問題意識編でした。今回は M2 マイルストーン (JPYC送金 + Spending Policy) の実装編 です。実装過程で「最初に書こうとした設計が JPYC の実装上の制約で成立しないことに気づき、別の道に切り替えた」というのが今回の中心的な物語で、最後に Polygon Amoy 上で 4 シナリオの実弾検証 までやりきっています。
記載の事実・コード・各チェーンの対応状況は2026年5月時点のものです。


 前回からの接続
前回の記事 では、「AIエージェン...

---

*この記事は自動収集システムによって保存されました。*
