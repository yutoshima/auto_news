---
title: "EmDash を pnpm の 7 日ルールで入れ直したら、つまずいたところ"
source: "Zenn"
category: "it"
published: 2026-10-13T14:56:02
url: https://zenn.dev/n_tong/articles/5ea0a290d8923d
---

# EmDash を pnpm の 7 日ルールで入れ直したら、つまずいたところ

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 14:56
- **URL**: [https://zenn.dev/n_tong/articles/5ea0a290d8923d](https://zenn.dev/n_tong/articles/5ea0a290d8923d)

## 概要

はじめに
前回、Astro 製の CMS「EmDash」を初期設定のまま試してみた。
https://zenn.dev/n_tong/articles/d764cb1e13d25c
EmDash が生成する pnpm-workspace.yaml のデフォルト設定は、「公開から 1 日未満の版は入れない」になっている。
今回は、これを自分の方針（Mini Shai-Huludなどの対策）に合わせて 7 日に延ばして入れ直してみた。
何か所かつまずいたので、記録しておく。

 作成
pnpm create emdash@latest
前回と同じく、こう答えた。

Project nam...

---

*この記事は自動収集システムによって保存されました。*
