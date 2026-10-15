---
title: "【備忘録】CSSのstickyで作る、せり上がりながら背景が見える演出"
source: "Zenn"
category: "it"
published: 2026-10-14T05:59:58
url: https://zenn.dev/crayfisher_zari/articles/75619d5860f885
---

# 【備忘録】CSSのstickyで作る、せり上がりながら背景が見える演出

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 05:59
- **URL**: [https://zenn.dev/crayfisher_zari/articles/75619d5860f885](https://zenn.dev/crayfisher_zari/articles/75619d5860f885)

## 概要

時々作っては作り方を忘れるので備忘録も兼ねて記事にします。正式名称を知らないのですが、スクロールしていくと前景のコンテンツがカーテンみたいにせり上がって背景が見えてくる演出のやつです。
▼こういうやつ


 position: stickyを使うメリット
position: fixedで背景に固定するのもいいですが、全体のレイアウトに影響があり関係ない要素まで副作用に巻き込まれるおそれがあります。position: stickyを使うとこの演出前後のみに影響を抑えられるのでコントロールがしやすいです。

 実装ポイント
模式的に3つのセクションにわけて説明します。せり上がる要素がセクショ...

---

*この記事は自動収集システムによって保存されました。*
