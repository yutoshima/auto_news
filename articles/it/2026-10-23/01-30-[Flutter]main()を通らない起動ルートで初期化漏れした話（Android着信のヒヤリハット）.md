---
title: "[Flutter]main()を通らない起動ルートで初期化漏れした話（Android着信のヒヤリハット）"
source: "Zenn"
category: "it"
published: 2026-10-23T01:30:05
url: https://zenn.dev/lincwell_inc/articles/ab2a642ea8f6f0
---

# [Flutter]main()を通らない起動ルートで初期化漏れした話（Android着信のヒヤリハット）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 01:30
- **URL**: [https://zenn.dev/lincwell_inc/articles/ab2a642ea8f6f0](https://zenn.dev/lincwell_inc/articles/ab2a642ea8f6f0)

## 概要

はじめに
Flutterアプリの初期化はmain()に書いておけばOK……と思っていたら、実はmain()を通らない起動ルートがありました。
気づいたきっかけは、APIリクエストにUser-Agentを付与するという小さな改修で、Androidの着信機能が鳴らなくなった現象が発生してしまいました。 リリース前に気づけたので本番影響はありませんでしたが、見落としやすいポイントだったので今回記事にしてみました。

 起きた問題
リリース予定のバージョンで、Androidのクリフォアコール（ビデオ通話の着信機能）が鳴らなくなっていました。
クリフォアコールについての説明はこちらの記事参照く...

---

*この記事は自動収集システムによって保存されました。*
