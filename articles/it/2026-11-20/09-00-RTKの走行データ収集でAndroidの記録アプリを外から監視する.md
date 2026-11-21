---
title: "RTKの走行データ収集でAndroidの記録アプリを外から監視する"
source: "Zenn"
category: "it"
published: 2026-11-20T09:00:06
url: https://zenn.dev/nauh_blog/articles/b60cd6973c8a3f
---

# RTKの走行データ収集でAndroidの記録アプリを外から監視する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 09:00
- **URL**: [https://zenn.dev/nauh_blog/articles/b60cd6973c8a3f](https://zenn.dev/nauh_blog/articles/b60cd6973c8a3f)

## 概要

こんにちは。ナウア株式会社の柳です。
私たちは、測定装置とエッジAI端末を組み合わせた調査機器を運用しています。
機器の状態を確かめたり設定を変えたりする管理画面は、自社で開発したWebアプリです。
研究・開発に使うため、車両で走行データを集めることもあります。
走行中の位置の記録に使うのは、RTKの受信機とAndroidのアプリ「DroggerGPS」（以下DrGPS）です。
データを集めるための走行には、車両とドライバーと時間がかかります。
途中で記録が止まっていても走行を終えるまで気づけなければ、その走行はやり直しです。
そこでDrGPSを監視するAndroidアプリを作り、記録で...

---

*この記事は自動収集システムによって保存されました。*
