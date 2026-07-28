---
title: "【決着】Claude CodeとCodexの設定ファイルを同期させる (みんな仲良く)"
source: "Zenn"
category: "it"
published: 2026-07-28T04:40:29
url: https://zenn.dev/explaza/articles/20f7f41cff8428
---

# 【決着】Claude CodeとCodexの設定ファイルを同期させる (みんな仲良く)

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月28日 04:40
- **URL**: [https://zenn.dev/explaza/articles/20f7f41cff8428](https://zenn.dev/explaza/articles/20f7f41cff8428)

## 概要

ごまんと触れられてきた話題であるのにも関わらず、細かい所に手の届くツールが無かったので作成しました。
有名どころから個人で制作されているツールまで、一通り使わせていただいたのですが実際に困った場面があり・・・

 サマリ
課題

同じプロジェクトでCodexとClaude Codeの両方を使っているとき、AGENTS.mdやSKILLSなどの変更が片方にしか適用されない
同期ツールは出ているものの、自動コピーやSymlinkの作成に留まり、差分があることを想定していない

目指すこと

設定ファイル群の自動同期
同期項目の制御
差分がある場合のマージサポート

やったこと

初回実行時...

---

*この記事は自動収集システムによって保存されました。*
