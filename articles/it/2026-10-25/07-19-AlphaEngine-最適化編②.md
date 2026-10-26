---
title: "AlphaEngine : 最適化編②"
source: "Zenn"
category: "it"
published: 2026-10-25T07:19:40
url: https://zenn.dev/reu/articles/0f77f6eb0940af
---

# AlphaEngine : 最適化編②

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 07:19
- **URL**: [https://zenn.dev/reu/articles/0f77f6eb0940af](https://zenn.dev/reu/articles/0f77f6eb0940af)

## 概要

はじめに
今回は最適化の続きとして全ピクセルや全フロクセルで行っていた
for (uint i = 0; i &lt; light_count; ++i)
をやめるべく
Clustered Lightingを実装してみた話をしていきたいと思います。

 Clustered Lighting
Clustered Lightingはカメラの視錐台を3Dグリッドに分割し、各クラスタに影響するライトだけをリスト化し、後段のライティング時に行う計算数を減らす最適化手段です。
詳細な説明は他のサイトにお願いします。
(頭の中に絵はあるけど言葉での説明がむずかしいでござ;;)
何がいいのかというと...

---

*この記事は自動収集システムによって保存されました。*
