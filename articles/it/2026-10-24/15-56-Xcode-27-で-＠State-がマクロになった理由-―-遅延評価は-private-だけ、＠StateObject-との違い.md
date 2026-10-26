---
title: "Xcode 27 で ＠State がマクロになった理由 ― 遅延評価は private だけ、＠StateObject との違い"
source: "Zenn"
category: "it"
published: 2026-10-24T15:56:27
url: https://zenn.dev/takehito/articles/50145459523321
---

# Xcode 27 で ＠State がマクロになった理由 ― 遅延評価は private だけ、＠StateObject との違い

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 15:56
- **URL**: [https://zenn.dev/takehito/articles/50145459523321](https://zenn.dev/takehito/articles/50145459523321)

## 概要

!
確認日：2026-10-24、2026-10-25
確認に使った環境は、Xcode 26.6（Build 17F113）、Xcode 27.1（Build 27A9275）、macOS 26.7.1 です。iOS 26.5 シミュレータ（Build 23F77）でも一部を確認しました。2026-10-25 には、@StateObject との比較、LazyState の計測、iOS シミュレータでの計測、そのほかの追加の計測をしました。Apple の SwiftUI リファレンスと移行ガイドも、同じ日に確認しました。記事の内容は、Apple の資料の改訂や Xcode の更新によって...

---

*この記事は自動収集システムによって保存されました。*
