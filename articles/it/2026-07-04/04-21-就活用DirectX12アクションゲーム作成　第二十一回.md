---
title: "就活用DirectX12アクションゲーム作成　第二十一回"
source: "Zenn"
category: "it"
published: 2026-07-04T04:21:33
url: https://zenn.dev/seisei89628/articles/cfec733913db02
---

# 就活用DirectX12アクションゲーム作成　第二十一回

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月04日 04:21
- **URL**: [https://zenn.dev/seisei89628/articles/cfec733913db02](https://zenn.dev/seisei89628/articles/cfec733913db02)

## 概要

※筆者は初学者なので、間違ったことを書いていれば教えてくれると助かります。

 はじめに
前回は、描画パスを整理しました。
Render() の中を、
DrawShadowMapPass();
DrawSceneColorPass();
DrawBackBufferPass();
という形に分け、SceneColorへ描いてからBackBufferへ貼る流れを見やすくしました。
今回は、この SceneColor Pass と BackBuffer Pass の間にBloomを追加します。
Bloomは、明るい部分をぼかして元の画像へ足すPost Effectです。
今回は最小構成として...

---

*この記事は自動収集システムによって保存されました。*
