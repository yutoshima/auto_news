---
title: "GitHub Actionsのコストが増えているなら、Namespaceを使えばいいじゃない"
source: "Zenn"
category: "it"
published: 2026-07-29T23:52:26
url: https://zenn.dev/aircloset/articles/6b47018589df0f
---

# GitHub Actionsのコストが増えているなら、Namespaceを使えばいいじゃない

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月29日 23:52
- **URL**: [https://zenn.dev/aircloset/articles/6b47018589df0f](https://zenn.dev/aircloset/articles/6b47018589df0f)

## 概要

!
English Version is here

みなさまこんにちは！エアークローゼットでCTOをしている辻です。
GitHub ActionsのランナーをGitHub hosted→Blacksmith→Namespaceと2回乗り換えました。結果を先に言うと:

CIコストはGitHub hosted時代の約1/4
遅い処理（p90）でも37%短縮
CIが完了しない事故は32件→0件
移行作業は1行変えるだけ

この記事はその実測記録です。乗り換え判断の材料になるよう、測り方も失敗談も込みで公開します。

 AIで開発すると、CIは静かに膨らみ続ける
まず課題感から。AIエージェ...

---

*この記事は自動収集システムによって保存されました。*
