---
title: "JAXで「行列が小さいのに遅い」謎はなぜ？XLAカーネル融合の落とし穴と最適化"
source: "Qiita (Python)"
category: "it"
published: 2026-02-11T14:07:22
url: https://qiita.com/boku_research/items/9ec1d8893ef5ec7fbb7d
---

# JAXで「行列が小さいのに遅い」謎はなぜ？XLAカーネル融合の落とし穴と最適化

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年02月11日 14:07
- **URL**: [https://qiita.com/boku_research/items/9ec1d8893ef5ec7fbb7d](https://qiita.com/boku_research/items/9ec1d8893ef5ec7fbb7d)

## 概要

※この記事は、個人技術ブログ CodeArchPedia.com の技術メモ（要約）です。
JAXを使ってGPU上でバッチ行列積を試した際、内側の次元Kが小さい方が結果的に遅くなるという奇妙な現象に遭遇した。機械学習モデルの性能検証中にこのボトルネックを見つけ、原因究明のた...

---

*この記事は自動収集システムによって保存されました。*
