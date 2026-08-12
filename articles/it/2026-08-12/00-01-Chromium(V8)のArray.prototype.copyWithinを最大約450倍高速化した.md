---
title: "Chromium(V8)のArray.prototype.copyWithinを最大約450倍高速化した"
source: "Zenn"
category: "it"
published: 2026-08-12T00:01:18
url: https://zenn.dev/dinii/articles/a272b7c3b60ab8
---

# Chromium(V8)のArray.prototype.copyWithinを最大約450倍高速化した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月12日 00:01
- **URL**: [https://zenn.dev/dinii/articles/a272b7c3b60ab8](https://zenn.dev/dinii/articles/a272b7c3b60ab8)

## 概要

はじめに
!
修正や追加等はコメントまたはGitHubで編集リクエストをお待ちしております。

ダイニーで一番若いエンジニアのriya amemiya(21歳)です。
これまで Array.prototype.flat を2回にわたって高速化してきましたが、今回は Array.prototype.copyWithin（以下 copyWithin）を最大約450倍高速化しました。
「copyWithinって何だっけ」となった方も多いはずです。ES2015から実はあります。
JS大改革のES6に実は入ってるメソッドなんですよね。flat や includes のようなメジャーなメソッドと...

---

*この記事は自動収集システムによって保存されました。*
