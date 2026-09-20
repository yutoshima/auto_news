---
title: "就活用DirectX12アクションゲーム作成　第三十二回"
source: "Zenn"
category: "it"
published: 2026-09-19T00:34:29
url: https://zenn.dev/seisei89628/articles/b505300dc8eaac
---

# 就活用DirectX12アクションゲーム作成　第三十二回

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月19日 00:34
- **URL**: [https://zenn.dev/seisei89628/articles/b505300dc8eaac](https://zenn.dev/seisei89628/articles/b505300dc8eaac)

## 概要

※筆者は初学者なので、間違ったことを書いていれば教えてくれると助かります。

 はじめに
前回までで、DirectX12による3D描画、TextureとMaterial、FBX、Animation、PhysX、Particle、Morph Target、Debug UI、2D画像と文字、2D / 3D音声まで動くようになりました。
ここまでの制作では、描画、物理、音声、入力などの機能をC++側へ順番に追加してきました。
ただ、実際にゲームを作り始めると、低レベルのEngine処理とPlayerやBossのようなゲーム固有処理を同じ場所へ増やし続けるのは扱いづらくなります。
そこで今回は、...

---

*この記事は自動収集システムによって保存されました。*
