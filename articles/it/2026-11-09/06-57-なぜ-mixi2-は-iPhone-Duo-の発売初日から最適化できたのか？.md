---
title: "なぜ mixi2 は iPhone Duo の発売初日から最適化できたのか？"
source: "Zenn"
category: "it"
published: 2026-11-09T06:57:46
url: https://zenn.dev/mixi/articles/b0ea64fded9503
---

# なぜ mixi2 は iPhone Duo の発売初日から最適化できたのか？

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月09日 06:57
- **URL**: [https://zenn.dev/mixi/articles/b0ea64fded9503](https://zenn.dev/mixi/articles/b0ea64fded9503)

## 概要

こんにちは！mixi2 エンジニアの久野です🍎
iPhone Duo（以下 Duo）の発売初日、mixi2 がすでに最適化されている！ と話題にしていただきました。

対応を早く進められた理由は、振り返るとこの 3 つです。

ボトムタブが独自実装だったため、縦配置に変更しやすかったこと
分割した画面の右側に表示したい推し機能が決まっていたこと
シミュレーターでの確認だけで、実機でも動くことを祈ってリリースする大胆さがチームにあったこと

mixi2 は Flutter で開発しており、go_router で管理する各タブの画面に、独自のタブバーを重ねています。
Flutter 標準の ...

---

*この記事は自動収集システムによって保存されました。*
