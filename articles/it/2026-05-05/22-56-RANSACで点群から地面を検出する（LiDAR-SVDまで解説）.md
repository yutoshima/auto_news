---
title: "RANSACで点群から地面を検出する（LiDAR / SVDまで解説）"
source: "Qiita (Python)"
category: "it"
published: 2026-05-05T22:56:35
url: https://qiita.com/niikun0209/items/3ce0f6ec809d79c6062d
---

# RANSACで点群から地面を検出する（LiDAR / SVDまで解説）

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年05月05日 22:56
- **URL**: [https://qiita.com/niikun0209/items/3ce0f6ec809d79c6062d](https://qiita.com/niikun0209/items/3ce0f6ec809d79c6062d)

## 概要

これは何？
点群データには必ずノイズが混ざっている。鳥、電線、測量誤差……。
そのノイズに引っ張られず、「本当のモデル（平面・直線など）」を見つけるアルゴリズムが RANSAC だ。
森林LiDARでの主な使いどころ：

地面（DEM）の検出
個木の幹軸の推定
建物屋根...

---

*この記事は自動収集システムによって保存されました。*
