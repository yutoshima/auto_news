---
title: "PHPを更新するつもりが環境移行に【後編】WordPress移行の問題とSlackアプリの実装"
source: "Zenn"
category: "it"
published: 2026-10-25T13:58:04
url: https://zenn.dev/hotaka_noda/articles/74a3b28185af5c
---

# PHPを更新するつもりが環境移行に【後編】WordPress移行の問題とSlackアプリの実装

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 13:58
- **URL**: [https://zenn.dev/hotaka_noda/articles/74a3b28185af5c](https://zenn.dev/hotaka_noda/articles/74a3b28185af5c)

## 概要

はじめに
PHPの脆弱性対応をきっかけに、Lightsail上のBitnami版WordPressからLightsail提供版へ移行しました。移行に合わせてCloudFrontとWAFを導入し、キャッシュ削除をSlackから実行できるようにしています。
前編で説明した構成へ移す際には、固定ページが404になるなど、DBとファイルのコピーだけでは解決しない問題がありました。ここでは初動と移行の判断、問題への対処、Slackアプリの実装をまとめます。
https://zenn.dev/hotaka_noda/articles/3b4c51ecfe561d

 最初の対応

 公開範囲を絞...

---

*この記事は自動収集システムによって保存されました。*
