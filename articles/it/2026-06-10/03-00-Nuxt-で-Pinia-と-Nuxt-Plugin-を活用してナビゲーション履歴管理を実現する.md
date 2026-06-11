---
title: "Nuxt で Pinia と Nuxt Plugin を活用してナビゲーション履歴管理を実現する"
source: "Zenn"
category: "it"
published: 2026-06-10T03:00:07
url: https://zenn.dev/comm_vue_nuxt/articles/3cd1271b0fb8a3
---

# Nuxt で Pinia と Nuxt Plugin を活用してナビゲーション履歴管理を実現する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月10日 03:00
- **URL**: [https://zenn.dev/comm_vue_nuxt/articles/3cd1271b0fb8a3](https://zenn.dev/comm_vue_nuxt/articles/3cd1271b0fb8a3)

## 概要

はじめに
Nuxt（Vue.js）を利用していて、サイト内・サイト外からの遷移の履歴を管理したい、ナビゲーションガード時ではなく、コンポーネントライフサイクルの mount/create Hook 時でも遷移前のページがどこであったかを判定した上で処理を書きたい などの実装に悩んだことはないでしょうか？
それもそのはず、現状 Nuxt 標準の useRouter(), useRoute() や vuejs/router だけでは、そういった実装を実現することはできません。 今回は、その実装方法とともにNuxtでナビゲーション履歴を管理する方法について詳しく深掘って行こうと思います。
...

---

*この記事は自動収集システムによって保存されました。*
