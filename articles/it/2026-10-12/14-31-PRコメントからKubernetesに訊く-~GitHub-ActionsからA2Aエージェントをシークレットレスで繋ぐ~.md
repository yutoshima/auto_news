---
title: "PRコメントからKubernetesに訊く ~GitHub ActionsからA2Aエージェントをシークレットレスで繋ぐ~"
source: "Zenn"
category: "it"
published: 2026-10-12T14:31:57
url: https://zenn.dev/hyeonjae/articles/secretless-a2a-github-actions-ja
---

# PRコメントからKubernetesに訊く ~GitHub ActionsからA2Aエージェントをシークレットレスで繋ぐ~

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月12日 14:31
- **URL**: [https://zenn.dev/hyeonjae/articles/secretless-a2a-github-actions-ja](https://zenn.dev/hyeonjae/articles/secretless-a2a-github-actions-ja)

## 概要

A2Aエージェントを活用するにあたって、セキュリティの観点からどのように補強していったかを整理します。

 1. 背景
まず現在の状況を分かりやすく整理します。私たちは main ブランチにマージする前に、 k8s クラスタ上の job の状態を把握する必要がありました。
そのため GitHub で PR を上げた状態で、複数の開発者が実際に k8s クラスタへ接続して各種リソースの状態を確認していました。しかし k8s クラスタに接続するたびに VPN へ繋ぐ必要があり、手作業でリソースをひとつずつ点検するのは非常に時間がかかり煩雑な作業です。(もちろんミスも起こりえます！)
そこで「...

---

*この記事は自動収集システムによって保存されました。*
