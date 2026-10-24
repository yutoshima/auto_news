---
title: "Chromium(V8)のArray.prototype.fillを最大約7倍高速化した"
source: "Zenn"
category: "it"
published: 2026-10-20T01:00:05
url: https://zenn.dev/dinii/articles/5b8edc7856c25b
---

# Chromium(V8)のArray.prototype.fillを最大約7倍高速化した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月20日 01:00
- **URL**: [https://zenn.dev/dinii/articles/5b8edc7856c25b](https://zenn.dev/dinii/articles/5b8edc7856c25b)

## 概要

はじめに
!
修正や追加等はコメントまたはGitHubで編集リクエストをお待ちしております。

ダイニーで一番若いエンジニアのriya amemiya(21歳)です。
(V8の配列系メソッド高速化職人をそろそろ名乗っても怒られないんじゃないか？と最近思い始めました🧐)
今回は Array.prototype.fill（以下 fill）をSmiとdouble向けに最大約7倍高速化しました。
V8の配列系メソッドのfast path実装に取り組む人は世界で見てもほとんどいないので、この記事から少しでも興味を持っていただけると嬉しいです。
パッチはこちらです。
https://chromi...

---

*この記事は自動収集システムによって保存されました。*
