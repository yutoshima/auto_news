---
title: "ros_gzの終了時クラッシュとRange変換の不具合を修正した話"
source: "Zenn"
category: "it"
published: 2026-10-24T18:15:57
url: https://zenn.dev/yuu7/articles/ros2-gazebo-teardown-range-fixes
---

# ros_gzの終了時クラッシュとRange変換の不具合を修正した話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 18:15
- **URL**: [https://zenn.dev/yuu7/articles/ros2-gazebo-teardown-range-fixes](https://zenn.dev/yuu7/articles/ros2-gazebo-teardown-range-fixes)

## 概要

ROS 2とGazeboをつなぐros_gzに送った修正PRが、2026年10月13日に2件マージされました。
一つは画像ブリッジの終了時に発生するuse-after-free、もう一つは距離センサーが何も検出していないのにmax_range + 1を返す問題です。前者は終了処理とコールバックの同期、後者はセンサーメッセージの値の意味を修正しています。

#981：image_bridgeの終了処理で起きる競合状態の修正
#982：LaserScanからRangeへの変換をREP 117に合わせる修正

以前にマージされた#976と#977については前編の記事にまとめています。今回の2件...

---

*この記事は自動収集システムによって保存されました。*
