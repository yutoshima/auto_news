---
title: "Sceneに大量のオブジェクトがあった時の軽量化を考える"
source: "Qiita (React)"
category: "it"
published: 2026-03-21T18:38:51
url: https://qiita.com/shota-hamamatsu/items/2816360897808a23b079
---

# Sceneに大量のオブジェクトがあった時の軽量化を考える

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年03月21日 18:38
- **URL**: [https://qiita.com/shota-hamamatsu/items/2816360897808a23b079](https://qiita.com/shota-hamamatsu/items/2816360897808a23b079)

## 概要

概要

Scene上に大量のオブジェクトが存在したときに、動作が重くなり、FPSも落ちる
それをどう対処していくかを考えてみる

要因分析

まず、フレーム処理が重くなる要因を考えてみる

updateMatrixWorldによるオーバーヘッド

Three.jsでは...

---

*この記事は自動収集システムによって保存されました。*
